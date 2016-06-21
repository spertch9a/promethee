# coding=utf-8
from math import exp

def usual_function(delta):
		if (delta>0):
			return 1;
		else:
			return 0;
def linear_function(delta):
	if (delta < 0):
		output = 0.0;
	elif (delta > 1):
		output = 2.0;
	else:
		output = (delta)/2.0;
	return output;
def gaussian_function(delta):
	res = exp(-(delta**2.0)/(2*0.21**2));
	return res;

preference_functions = {
	'usual': usual_function,
	'linear': linear_function,
	'gaussian': gaussian_function
};