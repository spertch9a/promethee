import random;
import csv;

def initialise_matrix(width,height):
	Matrix=[[0 for x in range(width)] for y in range(height)];
	return Matrix;
def initialize_array(length):
	array = [0 for x in range(length)];
	return array;

def random_matrix(width, height):
	matrix = [[random.random() for x in range(width)] for y in range(height)];
	return matrix;

def random_array(length):
	array = [random.random() for x in range(length)];
	return array

def random_normalized_array(length):
	array = random_array(length);
	arraySum = sum(array);
	for x in range(length):
		array[x] = array[x]/arraySum;
	return array;
## returns the result of the division of one integer by another integer
def divide_integers(numerator, denumerator):
	return float(numerator)/float(denumerator);

def write_table_to_csv(array,path_to_csv):
	with open(path_to_csv, 'w') as csvfile:
		writer = csv.writer(csvfile)
		[writer.writerow(r) for r in array]

def read_table_from_csv(path_to_csv):
	with open(path_to_csv, 'r') as csvfile:
		reader = csv.reader(csvfile)
		table = [[e for e in r] for r in reader]
	return table;