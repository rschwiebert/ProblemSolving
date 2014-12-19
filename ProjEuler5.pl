#!/usr/bin/perl
# https://projecteuler.net/problem=5

# Find the LCM of 1-20 

use warnings;
use strict;

sub euclidAlg{
    my ($x,$y) = sort{$b <=> $a} @_ ;
    while ($x % $y != 0){
        ($x, $y)=($y, $x % $y);
    }
    return $y;
}

sub myLCM{
    return ( $_[0] * $_[1] ) / &euclidAlg(@_);
}

my $answer = 2;
my $i = 0;

for $i (3..20){
    $answer = &myLCM($answer, $i);
}

print "The answer is: $answer\n";



exit;
