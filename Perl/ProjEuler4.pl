#!/usr/bin/perl
# https://projecteuler.net/problem=4

# largest palindromic number that's a product of three digit numbers

use warnings;
use strict;

my($i,$j,$p,$maxNum)=(0,0,0,0);

for $i (1..999){
    for $j (($i+1)..999){
        $p = $i*$j;
        if ( ($p > $maxNum) && ("$p" eq reverse "$p") ){
            $maxNum = $p;
        }
    }
}

print "The answer is: $maxNum\n";

exit;
