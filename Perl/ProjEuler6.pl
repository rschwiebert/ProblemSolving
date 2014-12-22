#!/usr/bin/perl
# https://projecteuler.net/problem=6

# Find sum squared minus sum of squares for first 100 natural numbers

use warnings;
use strict;
use List::Util;

my ($sum1,$sum2,$i)=(0,0,0);

$sum1 = &List::Util::sum(1..100);
$sum1 = $sum1**2;

my @array = map {$_**2} (1..100);
$sum2 = &List::Util::sum(@array);

my $answer = $sum1 - $sum2;

print "The answer is: $answer\n";

exit;
