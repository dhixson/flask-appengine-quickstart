import argparse
import MySQLdb
import time
from google.cloud import spanner
from pprint import pprint

spanner_client = spanner.Client()
instance_id = 'test-instance'
instance = spanner_client.instance(instance_id)
database_id = 'example-db'
database = instance.database(database_id)

def load_products(cursor, org_id):
    query = """SELECT id, name, slug, short_description, user_id, type_id,
                created_at, deleted_at, min, max, tax_class, variant_label
            FROM products"""
    cursor.execute(query)
    products = cursor.fetchall()
    print "Loading %d Products" % len(products)
    time1 = time.time()
    with database.batch() as batch:
        for i in range(len(products) / 10):
            batch.insert(
                table='Products',
                columns=('product_id', 'name', 'slug', 'description', 'user_id',
                         'type_id', 'created_at', 'deleted_at', 'min', 'max',
                         'tax_class', 'variant_label', 'org_id'),
                values = [row+(org_id,) for row in products[i*10:i*10+10]]
            )
        batch.insert(
            table='Products',
            columns=('product_id', 'name', 'slug', 'description', 'user_id',
                'type_id', 'created_at', 'deleted_at', 'min', 'max',
                'tax_class', 'variant_label', 'org_id'),
            values = [row+(org_id,) for row in products[(len(products)/10)*10:]]
        )

def load_variants(cursor, org_id):
    query = """SELECT variants.id, variants.product_id, variants.name,
                variants.option_label, variants.min, variants.max,
                variants.created_at, variants.updated_at, variants.deleted_at
            FROM variants JOIN products ON products.id=variants.product_id"""
    cursor.execute(query)
    variants = cursor.fetchall()
    print "Loding %d Variants" % len(variants)
    time1 = time.time()
    with database.batch() as batch:
        for i in range(len(variants) / 10):
            batch.insert(
                table="Variants",
                columns=('variant_id', 'product_id', 'name', 'option_label', 'min',
                         'max', 'created_at', 'updated_at', 'deleted_at', 'org_id'),
                values = [row+(org_id,) for row in variants[i*10:i*10+10]]
            )
        batch.insert(
            table="Variants",
            columns=('variant_id', 'product_id', 'name', 'option_label', 'min',
                     'max', 'created_at', 'updated_at', 'deleted_at', 'org_id'),
            values = [row+(org_id,) for row in variants[(len(variants)/10)*10:]]
        )

def load_items(cursor, org_id):
    query = """SELECT items.id, items.product_id, items.variant_id,
                items.weight, items.length, items.width, items.height,
                items.manufacturer_sku, items.is_default, items.created_at,
                items.updated_at, items.deleted_at, items.location,
                items.premium_shipping_cost
            FROM items JOIN variants ON items.variant_id=variants.id
            JOIN products ON items.product_id=products.id AND variants.product_id=products.id"""
    cursor.execute(query)
    items = cursor.fetchall()
    print "Loading %d Items" % len(items)
    time1 = time.time()
    for i in range(len(items) / 10):
        with database.batch() as batch:
            batch.insert(
                table='Items',
                columns=('item_id', 'product_id', 'variant_id', 'weight',
                         'length', 'width', 'height',
                         'sku', 'is_default',
                         'created_at', 'updated_at', 'deleted_at',
                         'location',
                         'org_id'),
                values = [(row[0],
                           row[1],
                           row[2],
                           float(row[3]) if row[3] is not None else None,
                           float(row[4]) if row[4] is not None else None,
                           float(row[5]) if row[5] is not None else None,
                           float(row[6]) if row[6] is not None else None,
                           row[7], (row[8] == 1),
                           row[9], row[10], row[11], row[12],
                           org_id) for row in items[i*10:i*10+10]]
            )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--db_host', dest='db_host', default='localhost')
    parser.add_argument('--db_user', dest='db_user', default='homestead')
    parser.add_argument('--db_pass', dest='db_pass', default='secret')
    parser.add_argument('--db_name', dest='db_name', default='homestead')
    parser.add_argument('--org_id',  dest='org_id', default=0)
    args = parser.parse_args()
    kahn = MySQLdb.connect(args.db_host, args.db_user, args.db_pass, args.db_name)
    cursor = kahn.cursor()
    load_products(cursor, args.org_id)
    load_variants(cursor, args.org_id)
    load_items(cursor, args.org_id)
    kahn.close()
