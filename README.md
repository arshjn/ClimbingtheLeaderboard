# ClimbingtheLeaderboard
Arcade Game leaderboard ranking system

This problem is taken from Hackerrank
https://www.hackerrank.com/challenges/climbing-the-leaderboard/

An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number 1 on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.


Input Format

The first line contains an integer n, the number of players on the leaderboard.
The next line contains n space-separated integers ranked[i], the leaderboard scores in decreasing order.
The next line contains an integer, m, the number games the player plays.
The last line contains  space-separated integers player[j], the game scores.

Output is rank after each play.

Sample Input:
7
100 100 50 40 40 20 10
4
5 25 50 120

Output:
6
4
2
1
