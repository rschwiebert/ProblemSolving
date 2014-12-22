#!/usr/bin/perl
# https://projecteuler.net/problem=3

use warnings;
use strict;

sub findPrimeFactor {
    my $i = 2;
    my $m = $_[0];
    while($i < ($m**0.5) + 1){
        if ($m % $i == 0) {
            return $i;
        } else {
            $i++;
        }
    }
    return $m;
}

my $input = 600851475143;
my $factor = 1;

while (1){
    $factor = &findPrimeFactor($input);
    if ($factor == $input){
        last;
    } else {
        $input /= $factor;
    }
}

print "The answer is: $factor\n";

exit;
