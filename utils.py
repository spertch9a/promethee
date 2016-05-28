import random;

def initialise_matrix(width,height):
	Matrix=[[0 for x in range(width)] for y in range(height)];
	return Matrix;

def random_matrix(width, height):
	matrix = [[random.random() for x in range(width)] for y in range(height)];
	return matrix;

def random_normalized_array(length):
	array = [random.random() for x in range(length)];
	arraySum = sum(array);
	for x in range(length):
		array[x] = array[x]/arraySum;
	return array;