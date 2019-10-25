from pyspark import SparkConf, SparkContext
import unittest2
import logging
from pyspark.sql import SparkSession


logging.getLogger('py4j.java_gateway').setLevel(logging.WARN)
logging.getLogger("py4j").setLevel(logging.WARN)


class PySparkTestCase(unittest2.TestCase):
    """
    SparkContext being created for each test
    """
    partition_num = 1

    def setUp(self):
        # Setup a new spark context for each test
        class_name = self.__class__.__name__
        self.spark_session = SparkSession.builder \
            .master("local") \
            .appName(class_name) \
            .config("spark.ui.showConsoleProgress", False) \
            .getOrCreate()
        self.sc = self.spark_session.sparkContext


class SampleTest(PySparkTestCase):
    def test_that_it_works(self):
        self.assertEqual(
            self.sc.parallelize(range(100), 10),
            range(100)
        )
