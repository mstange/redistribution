Models and Algorithms for Production Stock Transfer Problems
------------------------------------------------------------

I'm using this repository to store the code I'm producing as part of my diploma thesis. The thesis is about a problem of redistributing stock between different branches of a company in such a way that products which don't sell well in some branches but sell well in other branches are transferred to the latter branches, subject to some conditions.

The solution of the problem is derived using [CPLEX](http://www.ibm.com/software/integration/optimization/cplex-optimizer), a proprietary and very expensive MIP solver which you probably don't have access to, so the code I'm publishing here will be of limited utility.

In any case, here's an example output of the code in the `try00` directory:

    $ python user.py "../HR-Group Umlagerung.xls" 0
    Importiere Excel-Datei ../HR-Group Umlagerung.xls (Seite 0)...
    Löse Problem für Artikel 56414 mit 98 Versorgern und 98 Abnehmern...
    IBM ILOG License Manager: "IBM ILOG Optimization Suite for Academic Initiative" is accessing CPLEX 12 with option(s): "e m b q ".
    Tried aggregator 3 times.
    MIP Presolve eliminated 187 rows and 3018 columns.
    MIP Presolve modified 5080 coefficients.
    Aggregator did 49 substitutions.
    Reduced MIP has 611 rows, 7125 columns, and 40119 nonzeros.
    Reduced MIP has 7125 binaries, 0 generals, 0 SOSs, and 0 indicators.
    Presolve time =    0.13 sec.
    Found feasible solution after 0.14 sec.  Objective = 119.3700
    Probing fixed 1600 vars, tightened 0 bounds.
    Probing time =    0.20 sec.
    Clique table members: 54503.
    MIP emphasis: balance optimality and feasibility.
    MIP search method: dynamic search.
    Parallel mode: deterministic, using up to 8 threads.
    Root relaxation solution time =    0.08 sec.

            Nodes                                         Cuts/
       Node  Left     Objective  IInf  Best Integer    Best Bound    ItCnt     Gap

    *     0+    0                          119.3700                   1616     --- 
    *     0+    0                         2560.7900                   1616     --- 
          0     0     3539.4865   152     2560.7900     3539.4865     1616   38.22%
          0     0     3529.1730   158     2560.7900      Cuts: 48     1714   37.82%
          0     0     3522.6280   135     2560.7900      Cuts: 35     1848   37.56%
          0     0     3508.9048   143     2560.7900      Cuts: 34     2048   37.02%
    *     0+    0                         3441.2500     3508.9048     2254    1.97%
          0     0     3497.8572   129     3441.2500      Cuts: 26     2254    1.64%
          0     0     3489.1143   112     3441.2500      Cuts: 28     2369    1.39%
          0     0     3483.2783   108     3441.2500      Cuts: 22     2501    1.22%
          0     0     3479.1057   115     3441.2500      Cuts: 18     2687    1.10%
          0     0     3473.8070   108     3441.2500  ZeroHalf: 16     2786    0.95%
          0     0     3473.1842   115     3441.2500      Cuts: 26     2832    0.93%
          0     0     3469.2133    95     3441.2500  ZeroHalf: 20     2974    0.81%
          0     0     3468.9210    91     3441.2500  ZeroHalf: 18     3089    0.80%
          0     0     3468.0706    73     3441.2500  ZeroHalf: 13     3152    0.78%
          0     0     3463.1556    91     3441.2500      Cuts: 22     3212    0.64%
    *     0+    0                         3452.6000     3463.1556     3212    0.31%

    Repeating presolve.
    Tried aggregator 2 times.
    MIP Presolve eliminated 83 rows and 2105 columns.
    MIP Presolve modified 166 coefficients.
    Aggregator did 1 substitutions.
    Reduced MIP has 527 rows, 5019 columns, and 25912 nonzeros.
    Reduced MIP has 5019 binaries, 0 generals, 0 SOSs, and 0 indicators.
    Probing time =    0.00 sec.
    Tried aggregator 2 times.
    MIP Presolve eliminated 0 rows and 2 columns.
    Aggregator did 1 substitutions.
    Reduced MIP has 526 rows, 5016 columns, and 25908 nonzeros.
    Reduced MIP has 5016 binaries, 0 generals, 0 SOSs, and 0 indicators.
    Represolve time =    0.12 sec.
    Probing time =    0.00 sec.
    Clique table members: 2223.
    MIP emphasis: balance optimality and feasibility.
    MIP search method: dynamic search.
    Parallel mode: deterministic, using up to 8 threads.
    Root relaxation solution time =    0.09 sec.

            Nodes                                         Cuts/
       Node  Left     Objective  IInf  Best Integer    Best Bound    ItCnt     Gap

    *     0+    0                         3452.6000     3463.1556     5130    0.31%
          0     0     3463.1556   107     3452.6000     3463.1556     5130    0.31%
    *     0+    0                         3457.1500     3463.1556     5130    0.17%
          0     2     3463.1556   107     3457.1500     3463.1556     5130    0.17%
    Elapsed real time =   1.81 sec. (tree size =  0.01 MB, solutions = 7)
        380   343     3458.8156    32     3457.1500     3462.6019    10434    0.16%
    *   405+  363                         3457.8500     3462.6019    10612    0.14%
       1188   981     3461.0567    51     3457.8500     3462.3208    19744    0.13%
       2501  2116     3460.8233    40     3457.8500     3462.3208    35429    0.13%

    Clique cuts applied:  3
    Cover cuts applied:  3
    Implied bound cuts applied:  8
    Zero-half cuts applied:  49
    Gomory fractional cuts applied:  3

    Root node processing (before b&c):
      Real time             =    2.92
    Parallel b&c, 8 threads:
      Real time             =    1.79
      Sync time (average)   =    0.00
      Wait time (average)   =    0.00
                              -------
    Total (root+branch&cut) =    4.71 sec.

    -----------------

    Resultat:

    Filiale 2133 wird beliefert von folgenden Filialen: 2134
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME4, ME6
    Filiale 1347 wird beliefert von folgenden Filialen: 1360, 2112
      Dabei werden folgende Varianten überbeliefert: ME3, ME4, ME6
    Filiale 0103 wird beliefert von folgenden Filialen: 2004
      Dabei werden folgende Varianten überbeliefert: ME3
    Filiale 0956 wird beliefert von folgenden Filialen: 2150
      Dabei werden folgende Varianten überbeliefert: ME3, ME4, ME6
    Filiale 2001 wird beliefert von folgenden Filialen: 0152
      Dabei werden folgende Varianten überbeliefert: ME3
    Filiale 2098 wird beliefert von folgenden Filialen: 0192
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 0393 wird beliefert von folgenden Filialen: 2144
      Dabei werden folgende Varianten überbeliefert: ME6
    Filiale 2077 wird beliefert von folgenden Filialen: 2048, 0225
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 2102 wird beliefert von folgenden Filialen: 0083
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 0338 wird beliefert von folgenden Filialen: 2073
      Dabei werden folgende Varianten überbeliefert: ME2, ME3, ME6
    Filiale 1091 wird beliefert von folgenden Filialen: 0161
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 1351 wird beliefert von folgenden Filialen: 1344
      Dabei werden folgende Varianten überbeliefert: ME2, ME3, ME4
    Filiale 0068 wird beliefert von folgenden Filialen: 0305
      Dabei werden folgende Varianten überbeliefert: ME2, ME3
    Filiale 0914 wird beliefert von folgenden Filialen: 0131
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 1337 wird beliefert von folgenden Filialen: 0236
      Dabei werden folgende Varianten überbeliefert: ME5, ME6
    Filiale 2127 wird beliefert von folgenden Filialen: 0050
      Dabei werden folgende Varianten überbeliefert: ME4
    Filiale 2139 wird beliefert von folgenden Filialen: 1361
      Dabei werden folgende Varianten überbeliefert: ME1, ME3
    Filiale 1325 wird beliefert von folgenden Filialen: 2043
      Dabei werden folgende Varianten überbeliefert: ME3, ME5
    Filiale 0035 wird beliefert von folgenden Filialen: 0238
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 0339 wird beliefert von folgenden Filialen: 2034
      Dabei werden folgende Varianten überbeliefert: ME4, ME6
    Filiale 2182 wird beliefert von folgenden Filialen: 0251
      Dabei werden folgende Varianten überbeliefert: ME4
    Filiale 1326 wird beliefert von folgenden Filialen: 2069, 2072
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 0102 wird beliefert von folgenden Filialen: 0491
      Dabei werden folgende Varianten überbeliefert: ME2, ME3
    Filiale 0087 wird beliefert von folgenden Filialen: 0208, 2017
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 0285 wird beliefert von folgenden Filialen: 0377, 0292
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 0870 wird beliefert von folgenden Filialen: 0263, 0970
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 1144 wird beliefert von folgenden Filialen: 0200, 0049
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 1373 wird beliefert von folgenden Filialen: 0331
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME5, ME6
    Filiale 2002 wird beliefert von folgenden Filialen: 0218, 1333
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 2146 wird beliefert von folgenden Filialen: 2110
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 2176 wird beliefert von folgenden Filialen: 1154
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 2180 wird beliefert von folgenden Filialen: 0233, 0213
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 1334 wird beliefert von folgenden Filialen: 0930
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 1359 wird beliefert von folgenden Filialen: 0394
      Dabei werden folgende Varianten überbeliefert: ME2, ME4
    Filiale 0363 wird nicht beliefert.
    Filiale 1329 wird beliefert von folgenden Filialen: 0135
      Dabei werden folgende Varianten überbeliefert: ME5, ME6
    Filiale 2104 wird beliefert von folgenden Filialen: 2156
      Dabei werden folgende Varianten überbeliefert: ME5, ME6
    Filiale 2181 wird beliefert von folgenden Filialen: 0461
      Dabei werden folgende Varianten überbeliefert: ME5, ME6
    Filiale 0969 wird beliefert von folgenden Filialen: 0133, 2123
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 2149 wird beliefert von folgenden Filialen: 0141
      Dabei werden folgende Varianten überbeliefert: ME4, ME5
    Filiale 0051 wird beliefert von folgenden Filialen: 0137
      Dabei werden folgende Varianten überbeliefert: ME2, ME6
    Filiale 0385 wird beliefert von folgenden Filialen: 0937
      Dabei werden folgende Varianten überbeliefert: ME4, ME6
    Filiale 0413 wird beliefert von folgenden Filialen: 0318, 0473
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 0269 wird beliefert von folgenden Filialen: 0262
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 1064 wird beliefert von folgenden Filialen: 0943
      Dabei werden folgende Varianten überbeliefert: ME4, ME6
    Filiale 1269 wird beliefert von folgenden Filialen: 0477
      Dabei werden folgende Varianten überbeliefert: ME4, ME6
    Filiale 2049 wird beliefert von folgenden Filialen: 0150
      Dabei werden folgende Varianten überbeliefert: ME2, ME3
    Filiale 0076 wird beliefert von folgenden Filialen: 2114
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 0228 wird beliefert von folgenden Filialen: 0395
      Dabei werden folgende Varianten überbeliefert: ME3, ME6
    Filiale 0248 wird beliefert von folgenden Filialen: 0177
      Dabei werden folgende Varianten überbeliefert: ME3, ME6
    Filiale 0277 wird beliefert von folgenden Filialen: 0143
      Dabei werden folgende Varianten überbeliefert: ME3, ME6
    Filiale 1282 wird beliefert von folgenden Filialen: 0136
      Dabei werden folgende Varianten überbeliefert: ME3, ME6
    Filiale 2040 wird beliefert von folgenden Filialen: 0295
      Dabei werden folgende Varianten überbeliefert: ME4, ME5
    Filiale 2076 wird beliefert von folgenden Filialen: 0371
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 2178 wird beliefert von folgenden Filialen: 0298
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 0428 wird beliefert von folgenden Filialen: 0291
      Dabei werden folgende Varianten überbeliefert: ME1, ME5, ME6
    Filiale 1029 wird beliefert von folgenden Filialen: 2107
      Dabei werden folgende Varianten überbeliefert: ME1, ME5, ME6
    Filiale 1133 wird beliefert von folgenden Filialen: 0407
      Dabei werden folgende Varianten überbeliefert: ME1, ME4, ME5, ME6
    Filiale 1153 wird beliefert von folgenden Filialen: 0931
      Dabei werden folgende Varianten überbeliefert: ME1, ME5, ME6
    Filiale 1205 wird beliefert von folgenden Filialen: 0304
      Dabei werden folgende Varianten überbeliefert: ME1, ME5, ME6
    Filiale 1317 wird beliefert von folgenden Filialen: 0168
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME5, ME6
    Filiale 1336 wird beliefert von folgenden Filialen: 0374
      Dabei werden folgende Varianten überbeliefert: ME1, ME5, ME6
    Filiale 1356 wird beliefert von folgenden Filialen: 0221
      Dabei werden folgende Varianten überbeliefert: ME1, ME5, ME6
    Filiale 2129 wird beliefert von folgenden Filialen: 2042
      Dabei werden folgende Varianten überbeliefert: ME5, ME6
    Filiale 2177 wird beliefert von folgenden Filialen: 0972
      Dabei werden folgende Varianten überbeliefert: ME1, ME3, ME5, ME6
    Filiale 0030 wird beliefert von folgenden Filialen: 0264
      Dabei werden folgende Varianten überbeliefert: ME5, ME6
    Filiale 0423 wird nicht beliefert.
    Filiale 1139 wird beliefert von folgenden Filialen: 1365
      Dabei werden folgende Varianten überbeliefert: ME5, ME6
    Filiale 1260 wird nicht beliefert.
    Filiale 1307 wird beliefert von folgenden Filialen: 2171
      Dabei werden folgende Varianten überbeliefert: ME3, ME6
    Filiale 1316 wird beliefert von folgenden Filialen: 2067
      Dabei werden folgende Varianten überbeliefert: ME3, ME5
    Filiale 2096 wird beliefert von folgenden Filialen: 1370
      Dabei werden folgende Varianten überbeliefert: ME5, ME6
    Filiale 0309 wird beliefert von folgenden Filialen: 1371
      Dabei werden folgende Varianten überbeliefert: ME1, ME5, ME6
    Filiale 1372 wird beliefert von folgenden Filialen: 0175
      Dabei werden folgende Varianten überbeliefert: ME1, ME5, ME6
    Filiale 1665 wird beliefert von folgenden Filialen: 0052
      Dabei werden folgende Varianten überbeliefert: ME1, ME2, ME3, ME4, ME5, ME6
    Filiale 2015 wird nicht beliefert.
    Filiale 2143 wird nicht beliefert.
    Filiale 1363 wird beliefert von folgenden Filialen: 2063
      Dabei werden folgende Varianten überbeliefert: ME1, ME3
    Filiale 0072 wird beliefert von folgenden Filialen: 1352
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 1331 wird beliefert von folgenden Filialen: 2094
      Dabei werden folgende Varianten überbeliefert: ME4, ME6
    Filiale 0895 wird nicht beliefert.
      Dabei werden folgende Varianten überbeliefert: ME3
    Filiale 2041 wird nicht beliefert.
      Dabei werden folgende Varianten überbeliefert: ME4
    Filiale 2174 wird nicht beliefert.
    Filiale 0416 wird beliefert von folgenden Filialen: 1367
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 1017 wird beliefert von folgenden Filialen: 0169
      Dabei werden folgende Varianten überbeliefert: ME3, ME6
    Filiale 2091 wird nicht beliefert.
    Filiale 0159 wird nicht beliefert.
    Filiale 1327 wird nicht beliefert.
      Dabei werden folgende Varianten überbeliefert: ME3, ME4
    Filiale 2068 wird nicht beliefert.
      Dabei werden folgende Varianten überbeliefert: ME5
    Filiale 1318 wird nicht beliefert.
    Filiale 0057 wird nicht beliefert.
      Dabei werden folgende Varianten überbeliefert: ME4
    Filiale 0307 wird beliefert von folgenden Filialen: 0974
      Dabei werden folgende Varianten überbeliefert: ME2, ME3, ME4, ME5, ME6
    Filiale 0095 wird nicht beliefert.
      Dabei werden folgende Varianten überbeliefert: ME5
    Filiale 0325 wird nicht beliefert.
      Dabei werden folgende Varianten überbeliefert: ME5
    Filiale 0345 wird nicht beliefert.
      Dabei werden folgende Varianten überbeliefert: ME5
    Filiale 1353 wird nicht beliefert.
      Dabei werden folgende Varianten überbeliefert: ME6
    Filiale 2137 wird nicht beliefert.
      Dabei werden folgende Varianten überbeliefert: ME6
    Filiale 2054 wird nicht beliefert.
    Folgende Versorgerfilialen haben keine Abnehmer gefunden: 2138, 0368, 1385, 0903, 1369, 0193, 0203, 0303, 0421
    Zielfunktionswert: 3457.85
