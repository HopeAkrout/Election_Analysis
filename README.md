#Election_Analysis

##Project Overview

A Coloraado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Get a complete list of counties where votes were cast.
7. Calculate the total number of votes in each county.
8. Calculate the percentage of votes each county.
9. Determine which county had the largest turnout.

##Resources
-Data Source: election_results.csv
-Software: Python 3.7.6, Visual Studio Code, 1.68.1

##Election-Audit Results
The analysis of the elction show that:
-There were 369,711 votes cast in the election.

The counties where votes were cast were:
  - Arapahoe
  - Denver
  - Jefferson
 
The voting results showed:
  - Arapahoe tallied 24,801 votes cast, which is 6.7% of the total state-wide votes.
  - Denver tallied 306,055 votes cast, which is 82.8% of the total state-wide votes.
  - Jefferson tallied 38,855 votes cast, which is 10.5% of the total state-wide votes.

The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
  - Diana DeGette received 73.8% of the vote with 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.

The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote with 272,892 votes.

##Election-Audit Summary

This script can be used as a template for upcoming elections of any type, from governor to state senator.  The aspect that makes it most useful is that there isn't a limit to the number of candidates or counties, the list of candidates and counties can change from list of raw results, and there will be no need to edit the script in such a case.  The only refactoring needed will be if the .csv results file changes the location of the data.  For example, if future data lists the candidate name in column A instead of C, then line 50 should adjust the row accordingly for the data to be pulled correctly.

This script can also be modified for use in other areas of use outside of elections themselves.  It can be used for polling political parties (edit the script so that instead of "candidate", "party" is used to for the outcome) in order to determine which counties have a higher population of democrats, republicans, and so forth.  A third variable could be added quite easily if data is available to drill down into the voters themselves.  If they've registered for a particular political party but voted for an incumbant from a different party, another list and dictionary can be created (see rows 17--22) and add in party to the for loop and if statements so that the data can be added to the candidate_results as another factor.

Dependant on what data is able to be gathered around votes cast, this script can be used as is, modified slightly or duplicated throughout to add in additional data as desired.
