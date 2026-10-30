#!/usr/bin/env python3
"""Yo Tours · Real Alcázar de Sevilla — route map, edition of 30 Oct 2026.
A PDF made to be read on a phone: page 1 = the whole site with the route, the way in (Puerta del León), the way out
(Apeadero, 53, into the Patio de Banderas) and the three lengths; page 2 = the palaces (1–19, 31–34); page 3 = the
gardens (35–53); page 4 = the Cuarto Real Alto (20–30, upper floor, separate timed visit) for the two optional Extras;
then the stop table. Every space carries the Alcázar's own number from its official leaflet (the guide speaks those
numbers); every track is a coloured circle beside its number (hollow = Extra).
The plan is our own simplified drawing after the geometry of the Alcázar's official leaflet (Patronato, tríptico,
research/map/hi-2.png, 300 dpi; pixel coordinates below are in that image): building masses drawn by hand, garden beds,
pools and garden walls traced and simplified. Not to scale; the leaflet has no compass and neither has this plan.
Stops come from v5/tracks/NNN.perf.txt (@room "No. n · name", @title, @type, @section); lengths from
build/static/lengths.json (ESSENTIAL, HIGHLIGHTS; 034–035 are the Cuarto Real Alto Extras, outside the lengths).
Usage (from the guide folder): python3 build/route_map.py <bundle folder> [--png <dir>]
  -> <bundle>/Alcazar_Audio_Guide_Route.pdf"""
import json, math, os, re, sys, html, asyncio, glob

B = sys.argv[1]
PNG_DIR = sys.argv[sys.argv.index("--png") + 1] if "--png" in sys.argv else None
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TRACKS = os.path.join(ROOT, "v5", "tracks")
LENGTHS_JSON = os.path.join(HERE, "static", "lengths.json")
OUT_PDF = os.path.join(B, "Alcazar_Audio_Guide_Route.pdf")
FOOTER = "Yo Tours · Real Alcázar de Sevilla audio guide · 30 Oct 2026 edition · plan drawn from the Alcázar's official leaflet"

# ---------------------------------------------------------------- stops, from the track files
def read_track(path):
    head, body, seen = {}, [], False
    for line in open(path, encoding="utf-8"):
        if not seen:
            if line.strip() == "---": seen = True; continue
            m = re.match(r"^@(\w+):\s*(.*?)\s*$", line)
            if m: head[m.group(1)] = m.group(2)
        else: body.append(line)
    words = len(re.sub(r"\[[^\]]*\]", " ", "".join(body)).split()) if seen else 0
    return head, words

TR = {}
for f in sorted(glob.glob(os.path.join(TRACKS, "[0-9][0-9][0-9].perf.txt"))):
    n = int(os.path.basename(f)[:3]); h, w = read_track(f)
    room = h.get("room", ""); m = re.match(r"No\.\s*(\d+)\s*·\s*(.+)$", room)
    num, space = (int(m.group(1)), m.group(2).strip()) if m else (None, room.replace("Outside · ", "").strip())
    t = re.sub(r"^(?:CRA\s+)?\d+\s*·\s*", "", h.get("title", "")).strip()
    ttype = h.get("type", "R"); extra = ttype == "X" or t.startswith("Extra · ")
    t = t.replace("Extra · ", "")
    if " — " in t: t = t.split(" — ", 1)[1]
    TR[n] = dict(type=ttype, num=num, space=space, title=t, words=w, section=h.get("section", ""), extra=extra,
                 outside=room.startswith("Outside"))
if not TR: sys.exit("no track files in " + TRACKS)
NUMS = sorted(TR)
XS = {n for n in NUMS if TR[n]["extra"]}
CRA = {n for n in NUMS if "Cuarto Real Alto" in TR[n]["section"]}
MID = {"W": 300, "R": 230, "X": 190, "ANCHOR": 320, "CLOSE": 320}
def minutes(n):
    t = TR[n]; w = t["words"] if t["words"] > 40 else MID.get(t["type"], 230)
    return w / 125.0
def fmt_min(m):
    h = round(m * 2) / 2; whole = int(h)
    return f"{whole}½" if h - whole else f"{whole}"

# ---------------------------------------------------------------- the three lengths
J = json.load(open(LENGTHS_JSON, encoding="utf-8"))
H_SET = {int(x) for x in J["HIGHLIGHTS"].split()}; E_SET = {int(x) for x in J["ESSENTIAL"].split()}
OUTSIDE_LEN = {int(x) for x in J.get("EXTRAS_OUTSIDE_LENGTHS", "").split()} | CRA
F_SET = {n for n in NUMS if n not in OUTSIDE_LEN}
FX = len([n for n in F_SET if n in XS])
LENGTHS = [("Full tour", len(F_SET), "about 2 h", f"all {len(F_SET) - FX} main stops and {FX} short Extras"),
           ("Essential", len(E_SET), "about 1 h 15", "the main line, fewer stops in the gardens"),
           ("Highlights", len(H_SET), "about 45 min", "the great rooms, the Baths and the Mercury pool")]

# ---------------------------------------------------------------- palette & sections
PAPER, INK, MUTED, LINE, CTX = "#F6F1E7", "#1F1B17", "#776E62", "#D8CEBD", "#ECE5D7"
RED, GOLD, NAVY = "#C0262D", "#A9812F", "#1D2B4A"
SECS = {  # @section -> (short title, colour)
    "Opening": ("Welcome", "#3D3A36"),
    "The first courtyards": ("The first courtyards", "#8C6A2E"),
    "Casa de la Contratación": ("Casa de la Contratación", "#2C5A7E"),
    "Palace of King Pedro": ("Palace of King Pedro", "#7A3A5E"),
    "Gothic palace": ("Gothic palace", "#A4581B"),
    "The gardens": ("The gardens", "#2E6A52"),
    "Closing": ("The way out", "#3D3A36"),
    "Optional: Cuarto Real Alto": ("Cuarto Real Alto (optional)", "#5B4A8A"),
}
def colour(n): return SECS.get(TR[n]["section"], ("", INK))[1]
def short(n): return TR[n]["title"]

# ---------------------------------------------------------------- the plan (leaflet hi-2.png pixel coordinates)
# building masses: (key, fill, stroke, polygon rings)
BLD = [
    ("banderas_n", "#E9E3D7", "#CFC6B6", [[(1240, 625), (1352, 442), (1398, 333), (1604, 482), (1590, 500), (1770, 688), (1758, 698), (1375, 464), (1265, 636)]]),
    ("banderas_s", "#E9E3D7", "#CFC6B6", [[(1142, 890), (1228, 642), (1560, 850), (1492, 993), (1408, 1030), (1313, 972), (1252, 1012)]]),
    ("gate", "#E2DCD0", "#8F8473", [[(1313, 972), (1407, 1030), (1350, 1123), (1252, 1070)]]),
    ("north", "#E2DCD0", "#8F8473", [[(1612, 972), (1745, 826), (1862, 904), (1842, 948), (2078, 1072), (2054, 1104),
                                      (1852, 992), (1772, 1162), (1965, 1268), (1950, 1300), (1790, 1222), (1600, 1118), (1550, 1095)]]),
    ("annex", "#E2DCD0", "#8F8473", [[(1830, 838), (1872, 812), (1912, 840), (1880, 905), (1850, 895)]]),
    ("strip", "#E2DCD0", "#8F8473", [[(1940, 822), (1955, 812), (2142, 978), (2125, 1000)]]),
    ("south", "#E2DCD0", "#8F8473", [[(1640, 1690), (1652, 1668), (1792, 1735), (1792, 1792)]]),
    ("asistente", "#E8E1D6", "#B3A796", [[(1722, 1448), (1674, 1455), (1652, 1473), (1625, 1463), (1595, 1492), (1544, 1463), (1526, 1488),
                                          (1524, 1512), (1477, 1579), (1640, 1691), (1711, 1562), (1708, 1519), (1728, 1473)]]),
    ("contratacion", "#D7E3EE", "#6F93B3", [[(1416, 1264), (1427, 1283), (1582, 1396), (1585, 1412), (1557, 1452), (1573, 1474), (1595, 1482),
                                             (1625, 1458), (1664, 1478), (1665, 1457), (1681, 1439), (1740, 1447), (1736, 1429), (1459, 1214)]]),
    ("yeso", "#EADFC4", "#A88F5A", [[(1688, 1012), (1627, 985), (1568, 1097), (1578, 1124), (1610, 1121), (1630, 1085), (1655, 1076)]]),
    ("pedro", "#EEDDE6", "#9C6A86", [[(1822, 1280), (1798, 1335), (1776, 1349), (1779, 1380), (1709, 1529), (1725, 1546), (1849, 1600),
                                      (1945, 1629), (2061, 1385), (2033, 1381), (2006, 1353), (1964, 1346), (1892, 1308), (1870, 1310), (1857, 1292)],
                                     [(1911, 1348), (1975, 1381), (1939, 1472), (1924, 1480), (1860, 1447), (1896, 1356)],
                                     [(1790, 1462), (1818, 1474), (1808, 1497), (1781, 1485)]]),
    ("gothic", "#F3DCC4", "#C08550", [[(2067, 1055), (2026, 1097), (1916, 1307), (1921, 1320), (2030, 1356), (2053, 1332), (2083, 1337),
                                       (2093, 1317), (2069, 1297), (2075, 1275), (2090, 1258), (2125, 1263), (2133, 1245), (2112, 1232),
                                       (2109, 1216), (2128, 1190), (2156, 1194), (2178, 1154), (2160, 1134), (2162, 1116), (2137, 1100), (2132, 1084)]]),
    ("cra", "#E3DDF0", "#8C7DB5", [[(2134, 159), (2027, 400), (1980, 469), (2194, 569), (2210, 553), (2234, 555), (2288, 449), (2302, 446),
                                    (2341, 359), (2338, 319), (2295, 311), (2280, 292), (2231, 278), (2204, 248), (2217, 204)],
                                   [(2206, 298), (2268, 332), (2233, 418), (2217, 427), (2157, 394), (2191, 306)]]),
    ("cra30", "#E3DDF0", "#8C7DB5", [[(1748, 161), (1707, 214), (1719, 242), (1809, 314), (1846, 318), (1938, 400), (1994, 432), (2030, 382)]]),
]
INNER = [  # thin inner lines: the wall between the two Gothic halls (32 | 33); the triple arch between 1 and 4
    ([(2122, 1108), (2012, 1338)], "#C08550", .5),
]
PILLARS = [[(1592, 1168), (1608, 1176), (1596, 1196), (1580, 1188)], [(1566, 1214), (1584, 1222), (1572, 1242), (1555, 1234)],
           [(1540, 1258), (1558, 1266), (1546, 1286), (1529, 1278)]]
# where the leaflet prints each number (its own label positions; 19, 34 and the upper floor moved onto the space)
TAG = {1: (1476, 1145), 2: (1598, 1090), 3: (1640, 1032), 4: (1684, 1269), 5: (1760, 1342), 6: (1619, 1401), 7: (1589, 1449),
       8: (1637, 1581), 9: (1549, 1553), 10: (1917, 1414), 11: (1842, 1379), 12: (1817, 1439), 13: (1991, 1442), 14: (1954, 1544),
       15: (1872, 1515), 16: (1849, 1556), 17: (1779, 1525), 18: (1791, 1478), 19: (1716, 1424),
       31: (1899, 1131), 32: (2039, 1204), 33: (2081, 1231), 34: (2112, 1262), 35: (1779, 1662), 36: (2021, 1576), 37: (2067, 1479),
       38: (2136, 1342), 39: (2256, 1154), 40: (2369, 1181), 41: (2446, 1255), 42: (2355, 1439), 43: (2174, 1730), 44: (2588, 1639),
       45: (2524, 1789), 46: (2244, 1947), 47: (2742, 1816), 48: (3240, 2069), 49: (2983, 1168), 50: (2726, 834), 51: (2263, 1025),
       52: (2041, 956), 53: (1799, 912),
       20: (2035, 450), 21: (2000, 425), 22: (2075, 478), 23: (2160, 500), 24: (2218, 540), 25: (2296, 398), 26: (2314, 338),
       27: (2140, 322), 28: (2098, 300), 29: (2112, 386), 30: (1912, 350)}
CRA_NUMS = set(range(20, 31))
START_PT = (1196, 1040)          # outside the Puerta del León, on the Plaza del Triunfo
EXIT_PT = (1636, 826)            # out of the Apeadero into the Patio de Banderas
# the route: main line (dashed, arrows) and there-and-back branches (dotted)
MAIN = [
    [START_PT, (1290, 1048), (1400, 1112), (1560, 1150), (1590, 1100), (1560, 1158), (1555, 1212), (1640, 1272), (1745, 1350),
     (1800, 1362), (1872, 1372), (1965, 1412), (1925, 1497), (1858, 1535), (1784, 1512), (1798, 1470), (1858, 1425), (1872, 1372),
     (1800, 1362), (1745, 1350), (1712, 1300), (1782, 1232), (1830, 1205), (1880, 1150), (1985, 1160), (2045, 1215), (2105, 1268),
     (2150, 1300), (2165, 1250), (2215, 1180), (2300, 1150), (2400, 1205), (2465, 1258), (2500, 1360), (2560, 1520), (2585, 1625),
     (2545, 1760), (2420, 1870), (2280, 1925), (2420, 1940), (2600, 1890), (2760, 1870), (2950, 1980), (3180, 2060), (3270, 1820),
     (3240, 1500), (3030, 1230), (2900, 1080), (2740, 870), (2560, 820), (2400, 960), (2290, 1040), (2180, 1060), (2050, 980),
     (1940, 930), (1820, 905), (1700, 860), EXIT_PT]]
SPURS = [[(1590, 1100), (1638, 1040)], [(1640, 1272), (1600, 1380), (1592, 1440)],
         [(2150, 1300), (2090, 1460), (2030, 1565), (1960, 1660), (1830, 1655)]]

# traced and simplified from the leaflet (leaflet px): garden beds, pools, garden and precinct walls
GEO_GREEN = ("3071,2037 3091,2044 3119,2016 3164,1994 3178,2008 3171,2020 3199,2069 3214,2056 3206,2027 3150,1962;3218,1872 3164,1"
    "942 3219,2005 3232,2010 3241,1980 3240,1941;2186,1970 2170,1928 2173,1919 2147,1869 2096,1890 1970,1909 1894,1936 19"
    "56,1976 2009,2031 2052,2052 2102,2049 2130,2038 2159,2012;2093,1857 2097,1862 2133,1850 2101,1845;2062,1839 2039,182"
    "4 1995,1817 1987,1822 2035,1840 2037,1854 1827,1870 1809,1853 1703,1892 1569,1926 1569,1942 1552,1950 1560,2067 1641"
    ",2115 1661,2116 1739,2047 1821,1943 1942,1891 2046,1876 2058,1867;1626,2203 3250,2105 3120,2113 3093,2073 3081,2083 "
    "3065,2083 3053,2073 3050,2056 2987,2103 2976,2120 2811,2130 2768,2118 2723,2134 2601,2142 2569,2133 2510,2138 2473,2"
    "114 2438,2139 2419,2139 2403,2123 2403,2099 2423,2088 2438,2089 2451,2101 2461,2093 2440,2058 2400,2090 2396,2104 23"
    "72,2098 2368,2088 2440,2006 2449,1970 2446,1927 2427,1889 2406,1868 2351,1868 2351,1856 2386,1832 2331,1810 2279,180"
    "4 2231,1819 2181,1855 2181,1917 2198,1933 2210,1934 2318,1874 2328,1887 2315,1906 2314,1940 2294,1967 2254,1998 2226"
    ",2004 2206,1997 2155,2053 2280,2108 2330,2118 2336,2125 2332,2135 2258,2152 2253,2127 2160,2083 2111,2075 2052,2085 "
    "2001,2105 1953,2148 1951,2176 1902,2180 1898,2165 1962,2106 1963,2034 1951,1996 1868,1943 1838,1957 1806,1989 1789,2"
    "018 1790,2043 1774,2078 1762,2081 1751,2072 1683,2138 1675,2163 1681,2193|1794,2153 1806,2153 1823,2171 1821,2185 17"
    "89,2184|1875,2102 1885,2110 1875,2122 1865,2114|1893,2067 1907,2077 1895,2093 1883,2079|1810,2059 1822,2056 1848,206"
    "9 1849,2089 1835,2091 1810,2071;1883,1617 1877,1632 1886,1645 1858,1711 1903,1729 1914,1691 1950,1637;1987,1575 1969"
    ",1614 2019,1634 2036,1595;1737,1563 1689,1656 1793,1700 1831,1605|1765,1615 1776,1631 1762,1640 1751,1624;2264,1533 "
    "2232,1577 2228,1606 2305,1650 2350,1597 2348,1585 2275,1531;2016,1510 1998,1552 2046,1572 2065,1530;3299,1456 3286,1"
    "456 3269,1475 3280,1601 3239,1801 3241,1861 3261,1933 3262,2005 3275,2020;2697,1455 2647,1511 2646,1521 2600,1565 26"
    "44,1611 2689,1569 2692,1558 2702,1557 2747,1513;2863,1582 2817,1501 2752,1417 2728,1428 2799,1519 2813,1518 2822,152"
    "6 2821,1542 2851,1575 2851,1588 2837,1592 2831,1580 2785,1611 2783,1626 2659,1719 2559,1780 2548,1779 2531,1757 2473"
    ",1800 2453,1805 2424,1757 2403,1765 2402,1749 2382,1739 2374,1725 2259,1648 2268,1678 2243,1679 2217,1638 2201,1644 "
    "2201,1668 2177,1696 2200,1719 2202,1748 2233,1767 2233,1789 2290,1774 2272,1731 2282,1718 2317,1776 2372,1785 2394,1"
    "781 2411,1820 2446,1831 2448,1840 2436,1852 2462,1921 2469,1924 2524,1848 2485,1842 2486,1825 2546,1820 2576,1809 26"
    "57,1744 2664,1727 2682,1727 2791,1637 2806,1639 2853,1610|2832,1589 2837,1605 2827,1625 2807,1630 2798,1605 2821,158"
    "8;2416,1510 2342,1447 2312,1447 2306,1418 2229,1355 2171,1432 2170,1446 2157,1451 2108,1534 2107,1548 2099,1552 2085"
    ",1545 2035,1663 2022,1667 1972,1646 1927,1739 1969,1756 1981,1718 2005,1689 2019,1698 2006,1731 2032,1738 2059,1685 "
    "2089,1584 2101,1576 2116,1579 2124,1591 2106,1603 2102,1622 2113,1623 2117,1633 2070,1689 2093,1724 2058,1735 2058,1"
    "778 2068,1805 2082,1817 2095,1813 2129,1827 2172,1827 2210,1803 2205,1788 2190,1782 2154,1805 2111,1803 2091,1771 20"
    "94,1728 2114,1696 2126,1687 2155,1684 2155,1656 2177,1633 2175,1610 2142,1620 2134,1616 2133,1592 2160,1590 2116,156"
    "4 2114,1550 2126,1547 2189,1582 2216,1565 2247,1522 2243,1508 2173,1459 2173,1447 2187,1445 2255,1493 2284,1488 2287"
    ",1515 2359,1567 2373,1567;2600,1343 2346,1672 2419,1732 2532,1591 2546,1584 2613,1506 2614,1496 2629,1488 2677,1432|"
    "2423,1624 2437,1620 2449,1627 2447,1651 2422,1645|2477,1545 2494,1539 2512,1543 2521,1558 2518,1578 2486,1580 2476,1"
    "566|2563,1453 2587,1452 2593,1477 2569,1479;2129,1283 2079,1379 2136,1412 2200,1328;2492,1262 2481,1264 2463,1286 24"
    "45,1285 2422,1317 2423,1343 2399,1350 2357,1408 2359,1428 2436,1493 2497,1415 2498,1399 2517,1390 2573,1316;3212,122"
    "3 3210,1237 3196,1246 3190,1359 3204,1367 3202,1396 3228,1397 3239,1368 3253,1227;3159,1217 3062,1207 3061,1218 3049"
    ",1221 2942,1370 2949,1377 2945,1436 2931,1438 2925,1407 2914,1406 2892,1438 2872,1447 2843,1443 2823,1470 2894,1579 "
    "2908,1579 2934,1559 2944,1531 2973,1532 2970,1551 2984,1559 2984,1572 2903,1609 2897,1618 2982,1723 3002,1729 3002,1"
    "746 3041,1793 3055,1800 3055,1822 3041,1824 2997,1771 2991,1770 2987,1793 2968,1788 2966,1774 2986,1766 2890,1651 28"
    "53,1636 2816,1662 2923,1797 2936,1799 2936,1813 2914,1812 2720,1967 2720,1988 2697,1999 2577,1850 2566,1849 2505,190"
    "6 2465,1989 2461,2015 2470,2058 2494,2098 2521,2111 2544,2110 2603,2076 2613,2089 2591,2115 2671,2116 2746,2097 2770"
    ",2079 2808,2100 2845,2065 2864,2075 2873,2099 2918,2102 2964,2085 3033,2029 3022,2014 2955,2027 2922,2025 2914,2001 "
    "2918,1973 2883,1962 2955,1835 2971,1836 2975,1847 2972,1865 2962,1868 2949,1896 2951,1927 2961,1938 2987,1916 2989,1"
    "902 3001,1902 3048,1959 3039,1997 3049,2016 3135,1938 3068,1857 3070,1843 3082,1843 3146,1918 3180,1879 3213,1804 32"
    "23,1742 3205,1735 3201,1725 3211,1717 3226,1720 3219,1662 3225,1655 3242,1656 3248,1615 3245,1469 3223,1423 3190,142"
    "2 3186,1531 3207,1562 3205,1600 3141,1624 3117,1610 3099,1582 3105,1535 3141,1514 3146,1410 3078,1406 3067,1388 3088"
    ",1357 3098,1365 3096,1384 3149,1390 3150,1364 3166,1356 3173,1242 3160,1233|2804,2051 2814,2059 2804,2072 2794,2064|"
    "2830,2020 2844,2028 2832,2044 2820,2036|2661,2034 2689,2008 2699,2017 2740,2018 2753,2008 2790,2010 2800,2018 2786,2"
    "045 2758,2064 2742,2043 2703,2037 2671,2042|3155,1694 3170,1708 3156,1721 3145,1710|3026,1539 3037,1547 3027,1559 30"
    "16,1551|3063,1225 3081,1233 3083,1256 3069,1254 3059,1235;2371,1174 2315,1244 2314,1256 2302,1260 2246,1333 2321,139"
    "8 2341,1395 2382,1338 2381,1308 2409,1302 2434,1268 2423,1253 2437,1232 2435,1221;2192,1173 2150,1249 2190,1269 2225"
    ",1298 2273,1238 2252,1222 2232,1247 2203,1244 2187,1215 2207,1185;2925,1145 2786,1339 2797,1368 2772,1408 2809,1456 "
    "2827,1431 2816,1404 2826,1371 2815,1367 2815,1355 2841,1324 2874,1314 2962,1190 2953,1166;1415,1119 1402,1140 1445,1"
    "173 1457,1174 1462,1186 1509,1220 1528,1192 1479,1160 1466,1160 1460,1148;1816,1113 1787,1162 1813,1162 1826,1184 18"
    "51,1192 1930,1243 1958,1192;1443,1074 1426,1101 1474,1132 1486,1132 1491,1143 1541,1174 1563,1141 1499,1111;3184,103"
    "9 3082,1188 3160,1197 3164,1185 3176,1183;1872,1020 1842,1070 1906,1099 1982,1147 2009,1098;2165,998 2127,1044 2182,"
    "1082 2199,1079 2218,1055 2197,1040 2199,1024;3256,949 3210,1007 3200,1178 3214,1202 3249,1206 3257,1132;1987,863 197"
    "1,894 1941,924 1988,951 2002,949 2006,961 2051,985 2061,963 2088,941 2042,905 2029,906 2026,893|2028,910 2032,941 20"
    "02,946 1998,915;2379,862 2362,856 2329,885 2313,889 2298,918 2351,898;3323,798 3286,817 3277,951 3282,1132 3262,1397"
    " 3285,1405 3288,1419 3278,1432 3300,1433;2470,698 2377,827 2386,842 2407,845 2411,855 2385,887 2384,901 2368,909 236"
    "8,985 2442,1040 2455,1039 2459,1054 2513,1116 2530,1123 2559,1102 2587,1110 2601,1132 2596,1160 2579,1175 2559,1178 "
    "2540,1170 2526,1146 2506,1148 2513,1173 2499,1180 2461,1128 2417,1090 2387,1124 2285,1061 2271,1075 2427,1175 2439,1"
    "164 2449,1165 2455,1177 2447,1189 2610,1299 2631,1292 2651,1312 2638,1329 2710,1408 2717,1397 2707,1375 2711,1350 26"
    "03,1266 2601,1252 2665,1246 2672,1290 2728,1331 2763,1325 2815,1252 2807,1213 2834,1204 2853,1210 2907,1134 2801,106"
    "2 2700,981 2687,978 2681,967 2575,895 2459,803 2421,844 2409,844 2407,830 2493,717|2509,1184 2523,1182 2586,1229 259"
    "2,1246 2578,1248 2515,1202|2706,1139 2746,1136 2754,1175 2713,1182 2703,1161|2632,1052 2640,1091 2590,1110 2592,1055"
    "|2479,972 2520,969 2528,1008 2487,1016 2477,995;3259,691 3131,874 3117,882 3085,938 3074,941 2947,1117 2971,1138 300"
    "1,1136 3117,973 3117,961 3131,959 3150,933 3172,942 3197,937 3207,951 3204,965 3213,967 3210,937 3192,926 3162,929 3"
    "142,884 3153,876 3200,894 3227,896 3257,873 3274,816;2564,671 2478,776 2575,848 2611,844 2618,880 2687,931 2723,927 "
    "2729,962 2801,1015 2837,1011 2843,1046 2928,1108 2995,1014 2988,984 2923,936 2891,936 2884,907 2818,858 2797,867 277"
    "0,863 2758,840 2757,813 2696,768 2663,771 2656,739;3331,587 3309,604 3295,643 3301,666 3327,700;2749,448 2675,537 26"
    "75,548 2663,551 2579,653 2670,721 2699,722 2707,748 2773,797 2818,796 2831,840 2896,888 2926,888 2935,916 2999,964 3"
    "033,963 3089,885 3086,851 3117,846 3181,758 3174,738 3107,688 3072,687 3064,657 2993,604 2958,603 2950,573 2879,520 "
    "2846,521 2838,490 2782,448|3016,764 3026,808 2981,813 2973,768|2902,680 2912,724 2867,729 2860,684|2790,597 2800,641"
    " 2755,646 2747,601;2485,683 2506,696 2551,631 2688,467 2676,445 2747,342 2757,354 2746,381 2760,405 3189,714 3214,70"
    "3 3259,640 3293,556 3311,546 3332,547 3332,530 3296,508 3203,704 3190,708 2760,391 2754,379 2784,316 2769,311 2776,2"
    "88 2759,278 2633,455 2643,467 2641,476 2584,527 2595,533 2595,545 2575,554 2551,579 2559,592 2556,611 2540,623 2519,"
    "614 2504,630 2512,644")
GEO_WATER = ("2426,2090 2410,2098 2404,2115 2413,2133 2432,2138 2448,2128 2452,2109 2442,2094;2992,1938 2946,1980 2951,1996 2967,2"
    "000 3011,1958;2499,1728 2446,1767 2462,1789 2515,1750;2158,1711 2139,1714 2135,1720 2128,1718 2114,1753 2120,1756 21"
    "18,1764 2129,1779 2149,1777 2163,1767 2175,1738 2167,1736 2167,1727;3157,1556 3145,1563 3142,1574 3150,1587 3163,158"
    "9 3174,1580 3175,1568 3167,1558;1536,1534 1527,1546 1561,1571 1571,1559;2067,1446 2061,1458 2074,1464 2080,1452;2333"
    ",1412 2322,1421 2331,1432 2342,1423;3264,1399 3254,1407 3253,1421 3263,1431 3275,1431 3285,1420 3284,1408 3276,1400;"
    "2975,1213 2892,1327 2903,1348 2926,1348 3005,1237;3178,1201 3177,1216 3195,1218 3196,1203;3011,1173 2997,1193 3018,1"
    "207 3032,1187;2264,1103 2220,1160 2296,1219 2344,1155;2616,1065 2609,1076 2618,1082 2626,1072;3125,1031 3103,1030 30"
    "23,1143 3054,1168 3136,1053;2321,1029 2296,1064 2389,1124 2414,1088;2012,921 2008,931 2018,935 2022,925;2908,903 290"
    "0,915 2910,922 2918,911;2790,804 2771,832 2800,851 2819,824;2998,781 2990,792 3000,800 3009,788;2680,737 2672,748 26"
    "82,756 2691,744;2772,614 2764,625 2774,633 2783,621")
GEO_WALL = ("3167,1993 3129,2016 3120,2015 3115,2019 3116,2025 3092,2044 3097,2059 3095,2073 3115,2098 3135,2085 3125,2068 3159,2"
    "041 3164,2043 3183,2077 3197,2070 3170,2021 3180,2012;1546,1946 1560,2147 1579,2148 1579,2132 1598,2132 1601,2180 16"
    "14,2182 1616,2210 3281,2111 3281,2103 3251,2104 3246,2110 1628,2205 1624,2201 1623,2176 1605,2174 1602,2126 1574,212"
    "8 1575,2142 1564,2143 1550,1950 1571,1941 1569,1925 1699,1892 1810,1851 1825,1869 2051,1855 2052,1848 1979,1822 1984"
    ",1830 1973,1853 1837,1861 1837,1848 1823,1835 1830,1790 1817,1797 1817,1835 1832,1849 1826,1860 1809,1847 1701,1887 "
    "1565,1921 1562,1925 1566,1938;2427,1759 2432,1778 2419,1788 2432,1808 2448,1800 2454,1807 2465,1809 2450,1793 2435,1"
    "804 2426,1798 2424,1788 2439,1779 2434,1764;2648,1717 2556,1776 2529,1751 2469,1800 2531,1756 2554,1782;1832,1709 18"
    "26,1723 1838,1739 1843,1727 1890,1748 1895,1760 1909,1766 1917,1760 1971,1784 1973,1790 1964,1818 1973,1821 1969,181"
    "3 2001,1737 1991,1737 1972,1774 1922,1752 1918,1745 1910,1756 1899,1752 1902,1738 1895,1740;2331,1683 2329,1689 2377"
    ",1726 2376,1734 2402,1748 2411,1744;;2202,1613 2298,1669 2211,1612;;2096,1547 2188,1607 2193,1604;2083,1535 2029,165"
    "1 2007,1643 1995,1651 1990,1648 1993,1638 1976,1631 1973,1645 2022,1666 1997,1723 2001,1731 2005,1731 2083,1546 2090"
    ",1544;;2439,1520 2317,1672 2307,1673 2316,1679;2025,1487 2020,1498 2043,1506 2046,1496;2117,1485 2113,1485 2093,1515"
    " 2058,1502 2055,1512 2092,1529;2720,1426 2707,1437 2709,1442 2719,1446 2833,1578 2794,1609 2809,1631 2814,1632 2830,"
    "1622 2827,1613 2837,1607 2835,1597 2856,1582 2821,1544 2824,1530 2810,1515 2799,1520;2076,1391 2070,1401 2092,1412 2"
    "096,1402;2059,1347 2047,1365 2066,1369 2075,1353;2220,1339 2210,1334 2140,1424 2108,1409 2102,1419 2144,1443;2625,13"
    "40 2685,1407 2688,1418 2696,1422 2708,1412 2706,1406 2697,1401 2638,1330;2594,1322 2446,1511 2591,1331;2096,1273 208"
    "5,1293 2103,1304 2116,1280;2298,1239 2288,1234 2225,1315 2232,1323 2238,1319;1821,1238 1815,1256 1825,1261 1837,1256"
    " 1859,1270 1861,1263 1837,1254 1840,1245 1845,1243 1866,1253 1878,1247 1840,1229;1562,1214 1544,1235 1557,1248 1575,"
    "1226;2134,1205 2125,1222 2143,1232 2156,1210;1588,1176 1571,1197 1584,1210 1601,1189;1626,1134 1598,1136 1608,1142 1"
    "601,1156 1609,1160;1338,1129 1442,1200 1451,1198 1412,1165 1356,1127;2199,1122 2223,1133 2233,1117 2219,1104 2241,10"
    "75 2255,1076 2261,1085 2274,1089 2279,1097 2286,1096 2291,1105 2301,1107 2306,1115 2314,1115 2318,1123 2329,1126 233"
    "3,1133 2341,1133 2348,1143 2356,1144 2361,1152 2453,1211 2455,1219 2462,1216 2491,1234 2491,1243 2497,1240 2596,1308"
    " 2600,1317 2605,1316 2618,1326 2640,1307 2627,1289 2611,1300 2449,1192 2447,1187 2456,1172 2440,1162 2428,1177 2273,"
    "1078 2271,1073 2282,1058 2271,1051 2244,1063;1281,1039 1252,1068 1270,1083 1267,1064;1409,1024 1412,1035 1560,1116 1"
    "552,1099 1543,1098;1872,1003 1938,1039 1935,1033 1942,1021 1929,1028 1917,1021 1916,1013 1911,1018 1893,1006;1983,97"
    "5 1987,982 2057,1021 2063,1019 2058,1008 2051,1011;1333,982 1312,972 1298,997 1305,1003 1299,1013 1306,1009 1319,986"
    ";3162,939 3155,953 3165,945 3174,949 3183,941 3199,947 3196,967 3202,972 3197,982 3201,985 3209,974 3201,966 3202,94"
    "5 3191,937 3172,944;1908,935 1975,973 1973,967 1912,933;1977,828 1977,848 1985,846 2106,942 2104,954 2113,948 2121,9"
    "54 2129,952 2009,859;1844,707 1730,844 1745,839 1858,906 1861,895 1849,894 1857,883 1853,882 1844,892 1748,833 1844,"
    "715 1940,804 1953,806;3335,575 3302,1433 3287,1435 3287,1454 3300,1456 3281,2004 3275,2074 3282,2074;3337,527 3326,5"
    "15 3293,502 3194,704 2760,383 2820,253 2810,247 2799,267 2787,264 2781,272 2764,262 2629,452 2472,617 2289,873 2238,"
    "983 2218,1013 2211,1016 2164,979 2164,987 2206,1020 2200,1035 2205,1039 2217,1037 2224,1042 2224,1051 2253,1041 2241"
    ",1027 2262,992 2260,985 2271,966 2255,953 2292,874 2311,849 2333,862 2322,847 2325,827 2339,817 2361,821 2480,647 24"
    "77,640 2513,604 2516,585 2528,576 2525,570 2554,539 2566,544 2619,489 2628,490 2644,467 2632,454 2756,280 2761,277 2"
    "783,289 2762,274 2766,268 2781,278 2791,269 2806,276 2754,385 3196,711 3294,509 3316,515 3332,526 3333,558 3337,558 "
    "3338,551")

def _dec(s):
    out = []
    for poly in s.split(";"):
        rings = [[tuple(int(v) for v in pt.split(",")) for pt in r.split()] for r in poly.split("|") if r.strip()]
        if rings: out.append(rings)
    return out

def esc(s): return html.escape(s, quote=True)
_uid = [0]
STOPS_AT = {}
for n in NUMS:
    k = TR[n]["num"] if TR[n]["num"] is not None else "OUT"
    STOPS_AT.setdefault(k, []).append(n)

def plan_svg(crop, width_mm, max_h_mm, nums=(), show=(), dots_off=None, notes=(), texts=(), overview=False, cra=False,
             tag_fs=2.3, route=True, filled=None, spurs=True):
    """crop = (x0, x1, y0, y1) in leaflet px. nums: map numbers to label. show: track numbers to draw as dots."""
    _uid[0] += 1; u = _uid[0]
    cx0, cx1, cy0, cy1 = crop; pad = 1.2
    S = min((width_mm - 2 * pad) / (cx1 - cx0), (max_h_mm - 2 * pad) / (cy1 - cy0))
    W = (cx1 - cx0) * S + 2 * pad; H = (cy1 - cy0) * S + 2 * pad
    def P(x, y): return pad + (x - cx0) * S, pad + (y - cy0) * S
    def path(rings): return " ".join("M" + " L".join(f"{P(*p)[0]:.2f},{P(*p)[1]:.2f}" for p in r) + " Z" for r in rings)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.2f} {H:.2f}" width="{W:.2f}mm" height="{H:.2f}mm">',
         f'<defs><clipPath id="c{u}"><rect x="0" y="0" width="{W:.2f}" height="{H:.2f}" rx="2"/></clipPath></defs>',
         f'<g clip-path="url(#c{u})"><rect x="0" y="0" width="{W:.2f}" height="{H:.2f}" fill="#FDFBF7"/>']
    sw = min(.75, max(.18, 7 * S))
    if not cra:
        for poly in _dec(GEO_GREEN): o.append(f'<path d="{path(poly)}" fill="#CFDFB4" fill-rule="evenodd"/>')
        for poly in _dec(GEO_WATER): o.append(f'<path d="{path(poly)}" fill="#AED3E6"/>')
        for poly in _dec(GEO_WALL): o.append(f'<path d="{path(poly)}" fill="#6E665B"/>')
    for k, fill, stroke, rings in BLD:
        if cra != k.startswith("cra"): continue
        dbg = ' fill-opacity=".45"' if os.environ.get("RM_UNDERLAY") else ""
        o.append(f'<path d="{path(rings)}" fill="{fill}"{dbg} fill-rule="evenodd" stroke="{stroke}" stroke-width="{sw:.2f}" stroke-linejoin="round"/>')
    if not cra:
        for pts, c, w in INNER:
            o.append(f'<path d="M{" L".join(f"{P(*p)[0]:.2f},{P(*p)[1]:.2f}" for p in pts)}" stroke="{c}" stroke-width="{max(.2, w * S * 10):.2f}" fill="none"/>')
        for pl in PILLARS: o.append(f'<path d="{path([pl])}" fill="#6E665B"/>')
    for x, y, t, cls, rot in texts:
        X, Y = P(x, y)
        tr = f' transform="rotate({rot} {X:.2f} {Y:.2f})"' if rot else ""
        o.append(f'<text x="{X:.2f}" y="{Y:.2f}" class="{cls}"{tr}>{esc(t)}</text>')
    # route
    def poly(pts, main_line):
        q = [P(*p) for p in pts]; d = "M" + " L".join(f"{a:.2f},{b:.2f}" for a, b in q)
        if main_line:
            o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".62" stroke-width="{.55 if not overview else .45}" stroke-dasharray="1.4,.9" stroke-linecap="round" stroke-linejoin="round"/>')
            for (xa, ya), (xb, yb) in zip(q, q[1:]):
                L = math.hypot(xb - xa, yb - ya)
                if L < (8 if not overview else 6): continue
                mx, my = (xa + xb) / 2, (ya + yb) / 2; a = math.degrees(math.atan2(yb - ya, xb - xa)); kk = 1.0 if not overview else .8
                o.append(f'<path d="M{-kk:.2f},{-kk * .8:.2f} L{kk:.2f},0 L{-kk:.2f},{kk * .8:.2f} Z" fill="{INK}" fill-opacity=".75" transform="translate({mx:.2f},{my:.2f}) rotate({a:.1f})"/>')
        else:
            o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity=".5" stroke-width=".42" stroke-dasharray=".2,.85" stroke-linecap="round"/>')
    if route:
        for s in (SPURS if spurs else []): poly(s, False)
        for m_ in MAIN: poly(m_, True)
    # notes (callouts), under the tags so they never hide a number
    for key, text, kind, dx, dy in notes:
        cx, cy = P(*key)
        colr = {"start": INK, "finish": INK, "info": MUTED, "warn": GOLD, "cra": "#5B4A8A"}[kind]
        fs = 2.4 if not overview else 2.2; lines = text.split("\n"); wmax = max(len(l) for l in lines) * fs * .55 + fs * 1.6
        hb = fs * 1.38 * len(lines) + fs * .62; tx, ty = cx + dx, cy + dy
        bx = min(max(tx - wmax / 2, .8), W - wmax - .8); by = min(max(ty - hb / 2, .8), H - hb - .8)
        o.append(f'<line x1="{cx:.2f}" y1="{cy:.2f}" x2="{bx + wmax / 2:.2f}" y2="{by + hb / 2:.2f}" stroke="{colr}" stroke-width=".35" stroke-dasharray="1,.7"/>')
        o.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r=".8" fill="{colr}"/>')
        o.append(f'<rect x="{bx:.2f}" y="{by:.2f}" width="{wmax:.2f}" height="{hb:.2f}" rx="{min(hb / 2, 2):.2f}" fill="{colr}"/>')
        for i, l in enumerate(lines):
            o.append(f'<text x="{bx + fs * .8:.2f}" y="{by + fs * 1.22 + i * fs * 1.38:.2f}" class="note" style="font-size:{fs:.2f}px">{esc(l)}</text>')
    # map numbers: red tag = a stop of this guide plays here; outlined = walk past
    stopnums = filled if filled is not None else {TR[n]["num"] for n in show if TR[n]["num"] is not None}
    tags = []
    for num in nums:
        if num not in TAG: continue
        X, Y = P(*TAG[num]); s = str(num); fs = tag_fs
        w = fs * (.62 * len(s) + .55); h = fs * 1.3
        if num in stopnums:
            tags.append(f'<rect x="{X - w / 2:.2f}" y="{Y - h / 2:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{h * .28:.2f}" fill="{RED}"/>'
                        f'<text x="{X:.2f}" y="{Y + fs * .36:.2f}" class="tg" style="font-size:{fs:.2f}px;fill:#fff">{s}</text>')
        else:
            tags.append(f'<rect x="{X - w / 2:.2f}" y="{Y - h / 2:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{h * .28:.2f}" fill="#fff" fill-opacity=".92" stroke="{RED}" stroke-width="{fs * .09:.2f}"/>'
                        f'<text x="{X:.2f}" y="{Y + fs * .36:.2f}" class="tg" style="font-size:{fs * .92:.2f}px;fill:{RED}">{s}</text>')
    o.extend(tags)
    # track dots, beside their map number
    rad = tag_fs * .78
    for k, st in STOPS_AT.items():
        st = [n for n in st if n in show]
        if not st: continue
        if k == "OUT": X, Y = P(*START_PT); base = (X, Y - rad * 1.6)
        else:
            X, Y = P(*TAG[k]); w = tag_fs * (.62 * len(str(k)) + .55)
            base = (X + w / 2 + rad * 1.15, Y)
        ddx, ddy = (dots_off or {}).get(k, (0, 0))
        if (dots_off or {}).get(("dir", k)) == "left":
            base = (X - (tag_fs * (.62 * len(str(k)) + .55)) / 2 - rad * 1.15, Y); step = -rad * 2.15
        else: step = rad * 2.15
        for i, s in enumerate(st):
            cx, cy = base[0] + ddx + i * step, base[1] + ddy
            c = colour(s)
            if s in XS:
                o.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad * .94:.2f}" fill="#fff" stroke="{c}" stroke-width="{rad * .2:.2f}"/>'
                         f'<text x="{cx:.2f}" y="{cy + rad * .34:.2f}" class="sn" style="font-size:{rad * .92:.2f}px;fill:{c}">{s}</text>')
            else:
                o.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{rad:.2f}" fill="{c}" stroke="#fff" stroke-width="{rad * .12:.2f}"/>'
                         f'<text x="{cx:.2f}" y="{cy + rad * .34:.2f}" class="sn" style="font-size:{rad * .95:.2f}px">{s}</text>')
    if os.environ.get("RM_UNDERLAY"):   # development aid: the leaflet under the drawing, to check the geometry
        o.insert(3, f'<image href="file://{os.environ["RM_UNDERLAY"]}" x="{P(0, 0)[0]:.2f}" y="{P(0, 0)[1]:.2f}" width="{3414 * S:.2f}" height="{2375 * S:.2f}" opacity=".8"/>')
    o.append("</g></svg>")
    return "".join(o), P, (W, H)

# ---------------------------------------------------------------- stop lists and dots in text
def dot(n, cls="dot"):
    c = colour(n)
    if n in XS: return f'<span class="{cls} hol" style="color:{c};border-color:{c}">{n}</span>'
    return f'<span class="{cls}" style="background:{c}">{n}</span>'
def tag(num, cls="tag"):
    if num is None: return f'<span class="{cls} out">out</span>'
    return f'<span class="{cls}">{num}</span>'
def stop_list(ns):
    rows = []
    for n in ns:
        t = TR[n]; c = colour(n); x = ' x' if n in XS else ''
        ex = f'<i style="color:{c}">Extra</i> ' if n in XS else ''
        rows.append(f'<div class="row{x}">{dot(n)}{tag(t["num"])}<span class="tt"><b>{esc(t["space"])}</b><br>{ex}{esc(short(n))}</span></div>')
    return "".join(rows)

# ---------------------------------------------------------------- page 1: the whole site
pages = []
lens = "".join(f'<div class="card"><div class="cnum" style="background:{NAVY}">{i}</div>'
               f'<div class="cbody"><div class="ct">{esc(n)}</div><div class="cs"><b>{esc(m)}</b> · {k} tracks</div><div class="cs2">{esc(d)}</div></div></div>'
               for i, (n, k, m, d) in enumerate(LENGTHS, 1))
MAIN_NUMS = sorted({TR[n]["num"] for n in NUMS if TR[n]["num"] is not None and n not in CRA})
ov, _, _ = plan_svg((1110, 3400, 640, 2262), 182, 140, nums=MAIN_NUMS, show=[], filled=set(MAIN_NUMS), overview=True, tag_fs=1.8,
    notes=[(START_PT, "IN · Puerta del León", "start", 3, -9), (EXIT_PT, "OUT · to the Patio de Banderas", "finish", 9, -8),
           ((1716, 1424), "19 · stair to the Cuarto Real Alto\nseparate timed visit · page 4", "cra", -23, 21)],
    texts=[(1440, 700, "Patio de Banderas", "yard", 0), (1215, 1112, "Plaza del Triunfo", "side", 0),
           (2318, 742, "Callejón del Agua", "side", -62), (2700, 1010, "The gardens", "zl", 0)])
KEYS = []
for sec, nums_ in (("The first courtyards", "1–5"), ("Casa de la Contratación", "6–7"), ("Palace of King Pedro", "10–18"),
                   ("Gothic palace", "31–34"), ("The gardens", "35–51"), ("Closing", "53")):
    KEYS.append(f'<span><i style="background:{SECS[sec][1]}"></i>{esc(SECS[sec][0])} <b>{nums_}</b></span>')
KEYS = "".join(KEYS)
pages.append(f'''<section class="page">
 <header><div class="brand">YO TOURS · AUDIO GUIDE</div><h1>Real Alcázar de Sevilla</h1>
 <p class="lede">Eleven centuries in one walk: the first courtyards, the palace of King Pedro, the Gothic palace and the gardens, {len(F_SET) - FX} main stops plus {FX} short Extras in one walking order. The guide comes in three lengths.</p></header>
 <div class="how"><div><b>1</b> <strong>The numbers are the Alcázar's own.</strong> The red numbers are the ones on its official leaflet, 1 to 53. The guide speaks them with the Spanish name: "number 15, the Salón de los Embajadores".</div>
 <div><b>2</b> The coloured circle beside a number is the track to play there, in track order. Hollow circles are short, optional Extras. A filled red number means a track plays there; an outlined one, you walk past.</div>
 <div><b>3</b> Each track ends by naming the next number. In Essential and Highlights a short line tells you where to go next. The plan is drawn simply, not to scale.</div></div>
 <div class="ov">{ov}<div class="keys">{KEYS}</div><div class="ovn">Red numbers: a track plays there. Pages 2 to 4 show every track beside its number.</div></div>
 <div class="warn"><b>In at the Puerta del León, out through the Apeadero (53) into the Patio de Banderas.</b> Once you are out you cannot come back in, so finish the gardens first. The Cuarto Real Alto upstairs (20–30) is a separate, timed visit; its two Extras are on page 4.</div>
 <div class="cards">{lens}</div>
 <footer>{esc(FOOTER)}</footer>
</section>''')

LEGEND = (f'<div class="legend"><span><span class="tag">15</span> Alcázar number, a track plays here</span>'
          f'<span><span class="tag ol">12</span> walk past</span>'
          f'<span>{dot(13, "ldot")} track</span><span><span class="ldot hol" style="color:{INK};border-color:{INK}">X</span> Extra</span>'
          f'<span><svg width="9mm" height="3mm" viewBox="0 0 9 3"><path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".6" stroke-width=".55" stroke-dasharray="1.4,.9"/></svg> route</span>'
          f'<span><svg width="9mm" height="3mm" viewBox="0 0 9 3"><path d="M.5,1.5 L8.5,1.5" stroke="{INK}" stroke-opacity=".5" stroke-width=".45" stroke-dasharray=".2,.8" stroke-linecap="round"/></svg> there and back</span></div>')

def map_page(title, sub, svg, ns, kicker, legend=True):
    return f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · REAL ALCÁZAR · {esc(kicker)}</div>
 <h2>{esc(title)}</h2><p class="sub">{sub}</p></header>
 <div class="stack"><div class="plan">{svg}{LEGEND if legend else ""}</div><div class="list">{stop_list(ns)}</div></div>
 <footer>{esc(FOOTER)}</footer>
</section>'''

# ---------------------------------------------------------------- page 2: the palaces
PAL = [n for n in NUMS if TR[n]["section"] in ("Opening", "The first courtyards", "Casa de la Contratación", "Palace of King Pedro", "Gothic palace")]
svg, _, _ = plan_svg((1150, 2205, 800, 1640), 182, 112, nums=list(range(1, 20)) + [31, 32, 33, 34, 53], show=PAL, tag_fs=2.3,
    dots_off={("dir", 7): "left", ("dir", 6): "left", 10: (0, -3.2), ("dir", 18): "left", ("dir", 2): "left", 5: (-.5, 1.2), 32: (-2.2, -3.4)},
    notes=[(START_PT, "START\nPuerta del León", "start", 4, 12), ((1736, 1438), "19 · stair to the\nCuarto Real Alto", "cra", -24, 4),
           ((2150, 1300), "to the gardens · page 3", "info", -2, 13), ((1700, 860), "OUT at the end\nto the Patio de Banderas", "finish", -12, 2)],
    texts=[(1222, 1112, "Plaza del Triunfo", "side", 0)])
pages.append(map_page("The palaces · 1 to 19 and 31 to 34",
    "Patio del León (1), Sala de la Justicia (2), Patio del Yeso (3) and back; the Montería (4) with the palace front (5) facing you and the Cuarto del Almirante (6, 7) on the right. "
    "Through the palace door to the Doncellas (10), the Embajadores (15) and the Muñecas (18); back out, and at the Montería's corner into the Crucero (31) and the Gothic palace (32, 33). "
    "You come out on the garden side by the Baths (34).", svg, PAL, "THE PALACES"))

# ---------------------------------------------------------------- page 3: the gardens
GAR = [n for n in NUMS if TR[n]["section"] in ("The gardens", "Closing")]
svg, _, _ = plan_svg((1650, 3395, 680, 2258), 182, 172, nums=list(range(34, 54)), show=GAR, tag_fs=2.4,
    dots_off={("dir", 35): "left", 51: (0, -.2)},
    notes=[(EXIT_PT, "OUT · Apeadero (53)\nto the Patio de Banderas", "finish", 13, -3)],
    texts=[(2318, 742, "Callejón del Agua", "side", -62), (3300, 1500, "Jardines de Murillo", "side", 87)])
pages.append(map_page("The gardens · 35 to 53",
    "From the Baths, down the Jardín de la Danza (38) through 37 and 36 to the Jardín del Príncipe (35) and back (Full only). Up to the Mercury pool (39), the Galería del Grutesco (40) and the Fuente de la Fama (41), "
    "through the formal gardens to the Pabellón de Carlos V (44) and the Cenador del León (45), round the outer gardens (46–50) and back to the Puerta de Marchena (51) and the Apeadero (53). "
    "Essential leaves this line after 44, Highlights after 39: follow the Salida signs to the Apeadero. The line is a guide; paths may be closed for maintenance.", svg, GAR, "THE GARDENS"))

# ---------------------------------------------------------------- page 4: the Cuarto Real Alto
CR = sorted(CRA)
svg, _, _ = plan_svg((1690, 2400, 140, 640), 182, 140, nums=list(range(20, 31)), show=CR, cra=True, route=False, tag_fs=3.0,
    texts=[(2212, 372, "courtyard", "yard", 0), (1880, 245, "Colección Carranza", "side", 38)])
pages.append(map_page("Optional · The Cuarto Real Alto, 20 to 30",
    "The upper floor of the palace of King Pedro, still a royal residence, is a separate, timed visit with its own guide. You reach it by the stair (19) in the corner of the Patio de la Montería, "
    f"where the palace front meets the Cuarto del Almirante. Our two Extras, {CR[0]} and {CR[-1]}, play there and are outside the three lengths. The second 11 the leaflet prints here is the open courtyard.",
    svg, CR, "UPPER FLOOR", legend=False))

# ---------------------------------------------------------------- pages 5+: the stop table
rows = []; last_sec = None
for n in NUMS:
    s = TR[n]["section"]
    if s != last_sec: rows.append(("sec", s)); last_sec = s
    rows.append(("stop", n))
chunks, cur = [], []
for r in rows:
    PER = 44 if not chunks else 48
    if len(cur) >= PER or (r[0] == "sec" and len(cur) >= PER - 2): chunks.append(cur); cur = []
    cur.append(r)
chunks.append(cur)
tot = {k: sum(minutes(n) for n in NUMS if f(n)) for k, f in (("F", lambda n: n in F_SET), ("E", lambda n: n in E_SET), ("H", lambda n: n in H_SET))}
for i, ch in enumerate(chunks):
    trs = []
    for kind, v in ch:
        if kind == "sec":
            c = SECS.get(v, ("", INK))[1]
            trs.append(f'<tr class="sh"><td colspan="7" style="color:{c};border-bottom-color:{c}">{esc(v)}</td></tr>')
        else:
            n = v; t = TR[n]; x = ' class="x"' if n in XS else ''
            ex = f'<i style="color:{colour(n)}">Extra</i> ' if n in XS else ''
            mk = lambda on: '<span class="mk">●</span>' if on else '<span class="no">·</span>'
            full = mk(True) if n in F_SET else '<span class="opt">optional</span>'
            trs.append(f'<tr{x}><td>{dot(n)}</td><td>{tag(t["num"])}</td><td class="tt"><b>{esc(t["space"])}</b> · {ex}{esc(short(n))}</td>'
                       f'<td class="mn">{fmt_min(minutes(n))}</td><td>{full}</td><td>{mk(n in E_SET)}</td><td>{mk(n in H_SET)}</td></tr>')
    if i == len(chunks) - 1:
        trs.append(f'<tr class="tot"><td colspan="3">Tracks · listening minutes (walking comes on top)</td><td class="mn"></td>'
                   f'<td>{len(F_SET)}<br><span>{round(tot["F"])}′</span></td><td>{len(E_SET)}<br><span>{round(tot["E"])}′</span></td><td>{len(H_SET)}<br><span>{round(tot["H"])}′</span></td></tr>')
    head = '<tr class="th"><th>#</th><th>No.</th><th>Stop</th><th>Min</th><th>Full</th><th>Essen&shy;tial</th><th>High&shy;lights</th></tr>'
    pages.append(f'''<section class="page">
 <header class="fh"><div class="brand">YO TOURS · REAL ALCÁZAR · ALL STOPS</div>
 <h2>The stops{" (continued)" if i else ""}</h2>
 {"" if i else f'<p class="sub">Every track in walking order: # on your player, No. on the Alcázar\'s leaflet, minutes of listening, and the lengths it belongs to (Full, {LENGTHS[0][2]}; Essential, {LENGTHS[1][2]}; Highlights, {LENGTHS[2][2]}; walking included). The Cuarto Real Alto Extras are optional.</p>'}</header>
 <table class="tbl">{head}{"".join(trs)}</table>
 <footer>{esc(FOOTER)}</footer>
</section>''')

CSS = f'''
@page {{ size: A4; margin: 0 }}
* {{ box-sizing: border-box }}
html, body {{ margin: 0; background: {PAPER}; color: {INK}; font-family: Inter, "DejaVu Sans", sans-serif }}
.page {{ width: 210mm; height: 297mm; padding: 13mm 13mm 10mm; position: relative; page-break-after: always; overflow: hidden; background: {PAPER} }}
.brand {{ font: 600 7.6pt Inter; letter-spacing: .28em; color: {GOLD} }}
h1 {{ font: 700 31pt Lora, serif; margin: 2mm 0 1mm; letter-spacing: -.01em }}
h2 {{ font: 700 19pt Lora, serif; margin: 2mm 0 1.2mm }}
.lede {{ font: 400 11pt Lora, serif; color: {MUTED}; margin: 0 0 3.5mm; line-height: 1.35 }}
.sub {{ font: 400 8.9pt Inter; color: {MUTED}; margin: 0 0 3mm; max-width: 184mm; line-height: 1.4 }}
.how {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 3mm; margin-bottom: 3mm }}
.how div {{ background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; padding: 2.2mm 2.8mm; font: 500 7.9pt Inter; line-height: 1.34 }}
.how b {{ display: inline-flex; width: 5mm; height: 5mm; border-radius: 50%; background: {INK}; color: #fff; font: 700 7.5pt Inter; align-items: center; justify-content: center; margin-right: 1.2mm }}
.how strong {{ color: {RED} }}
.ov {{ background: #fff; border: .3mm solid {LINE}; border-radius: 4mm; padding: 1.5mm 1mm; margin-bottom: 3mm }}
.ov svg {{ display: block; margin: 0 auto }}
.keys {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1mm 3mm; padding: 2mm 4mm 0; font: 500 6.9pt Inter; color: {INK} }}
.keys span {{ display: flex; align-items: center; gap: 1.3mm; white-space: nowrap }} .keys b {{ color: {MUTED}; font-weight: 600 }}
.keys i {{ width: 3mm; height: 3mm; border-radius: 50%; flex: none }}
.ovn {{ font: 500 6.8pt Inter; color: {MUTED}; text-align: center; padding: 1.4mm 0 .3mm }}
.zl {{ font: 700 2.6px Lora; fill: #8F8473; text-anchor: middle; letter-spacing: .1px }}
.warn {{ background: #fff; border: .3mm solid {GOLD}; border-left: 1.6mm solid {GOLD}; border-radius: 2.4mm; padding: 2.2mm 3mm; font: 400 8.2pt Inter; line-height: 1.38; margin-bottom: 3mm }}
.cards {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.4mm }}
.card {{ display: grid; grid-template-columns: 10mm 1fr; align-items: center; background: #fff; border: .3mm solid {LINE}; border-radius: 3mm; overflow: hidden; padding: 2mm 2mm 2mm 0 }}
.cnum {{ width: 7mm; height: 7mm; border-radius: 50%; color: #fff; font: 700 11pt Inter; display: flex; align-items: center; justify-content: center; margin-left: 2mm }}
.ct {{ font: 700 10.2pt Lora; margin-bottom: .4mm }} .cs {{ font: 400 7.9pt Inter; color: {MUTED} }} .cs b {{ color: {INK} }}
.cs2 {{ font: 400 7pt Inter; color: {MUTED}; margin-top: .4mm; line-height: 1.3 }}
footer {{ position: absolute; left: 13mm; right: 13mm; bottom: 7mm; font: 400 7pt Inter; color: {MUTED}; border-top: .3mm solid {LINE}; padding-top: 2mm }}
.stack .plan {{ margin-bottom: 3mm }} .stack .list {{ columns: 2; column-gap: 7mm }} .stack .row {{ break-inside: avoid }}
.plan {{ background: #fff; border: .3mm solid {LINE}; border-radius: 4mm; padding: 2mm }}
.plan svg {{ display: block; margin: 0 auto }}
.tg {{ font-family: Inter; font-weight: 800; text-anchor: middle }} .sn {{ font-family: Inter; font-weight: 700; fill: #fff; text-anchor: middle }}
.note {{ font-family: Inter; font-weight: 600; fill: #fff }}
.yard {{ font: 600 2.3px Inter; fill: #A39886; text-anchor: middle; letter-spacing: .4px; text-transform: uppercase }}
.side {{ font: 600 2.1px Inter; fill: #A39886; letter-spacing: .2px; text-anchor: middle }}
.legend {{ display: flex; flex-wrap: wrap; gap: 1.2mm 4mm; justify-content: center; padding: 2mm 1mm .4mm; font: 500 7pt Inter; color: {MUTED}; align-items: center }}
.legend > span {{ display: inline-flex; align-items: center; gap: 1.3mm }}
.ldot {{ width: 4.4mm; height: 4.4mm; border-radius: 50%; color: #fff; font: 700 6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.tag {{ display: inline-flex; min-width: 6mm; height: 4.4mm; padding: 0 1mm; border-radius: 1.2mm; background: {RED}; color: #fff; font: 800 7.4pt Inter; align-items: center; justify-content: center; box-sizing: border-box }}
.tag.ol {{ background: #fff; color: {RED}; border: .3mm solid {RED} }} .tag.out {{ background: #fff; color: {MUTED}; border: .3mm solid {LINE}; font-weight: 600; font-size: 6.4pt }}
.list .row {{ display: grid; grid-template-columns: 7.5mm 9.5mm 1fr; align-items: center; padding: .5mm 0; border-bottom: .25mm solid {LINE} }}
.dot {{ width: 6mm; height: 6mm; border-radius: 50%; color: #fff; font: 700 7.6pt Inter; display: inline-flex; align-items: center; justify-content: center }}
.hol {{ background: #fff; border: .45mm solid; box-sizing: border-box }}
.row.x .tt {{ color: {MUTED} }} .tt i {{ font-style: normal; font-weight: 700; font-size: 7pt; letter-spacing: .04em; margin-right: 1mm }}
.tt {{ font: 500 7.6pt Inter; line-height: 1.2 }} .tt b {{ font-weight: 700; color: {INK} }}
.tbl {{ width: 100%; border-collapse: collapse; background: #fff; border: .3mm solid {LINE}; border-radius: 3mm }}
.tbl th {{ font: 700 6.6pt Inter; color: {MUTED}; text-align: left; padding: 1.6mm 1.2mm 1.2mm; border-bottom: .35mm solid {INK}; letter-spacing: .04em; text-transform: uppercase }}
.tbl th:nth-child(n+4) {{ text-align: center; width: 13mm }} .tbl th:first-child {{ width: 9mm; padding-left: 2mm }} .tbl th:nth-child(2) {{ width: 11mm }}
.tbl td {{ padding: .12mm 1.2mm; line-height: 1.1; border-bottom: .2mm solid {LINE}; vertical-align: middle }}
.tbl td:first-child {{ padding-left: 2mm }} .tbl td:nth-child(n+4) {{ text-align: center }}
.tbl .dot {{ width: 4mm; height: 4mm; font-size: 6pt; vertical-align: middle }}
.tbl .tag {{ min-width: 5.4mm; height: 3.5mm; font-size: 6.3pt }}
.tbl .tt {{ font: 500 7.5pt Inter }} .tbl tr.x .tt {{ color: {MUTED} }}
.tbl .mn {{ font: 600 7.4pt Inter; color: {INK} }} .mk {{ color: {NAVY}; font-size: 8.4pt }} .no {{ color: #C9BFAE }}
.opt {{ font: 600 5.8pt Inter; color: #5B4A8A; letter-spacing: .02em }}
.tbl tr.sh td {{ font: 700 7.3pt Inter; padding: 1.2mm 2mm .4mm; border-bottom: .3mm solid; letter-spacing: .02em }}
.tbl tr.tot td {{ font: 700 7.6pt Inter; border-top: .35mm solid {INK}; border-bottom: none; padding: 1.6mm 1.2mm 1.6mm 2mm }} .tbl tr.tot span {{ font-weight: 500; color: {MUTED} }}
'''

def build():
    doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Real Alcázar de Sevilla · Yo Tours route</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
    os.makedirs(B, exist_ok=True)
    hp = os.path.join(B, "route_map.html"); open(hp, "w", encoding="utf-8").write(doc)
    async def render():
        from playwright.async_api import async_playwright
        async with async_playwright() as p:
            br = await p.chromium.launch(); pg = await br.new_page()
            await pg.goto("file://" + os.path.abspath(hp)); await pg.wait_for_timeout(300)
            await pg.pdf(path=OUT_PDF, format="A4", print_background=True, margin=dict(top="0", bottom="0", left="0", right="0"))
            if PNG_DIR:
                os.makedirs(PNG_DIR, exist_ok=True)
                await pg.set_viewport_size({"width": 794, "height": 1123})
                for i, el in enumerate(await pg.query_selector_all(".page")):
                    await el.screenshot(path=os.path.join(PNG_DIR, f"route_p{i+1}.png"), scale="device")
            await br.close()
    asyncio.run(render())
    if not os.environ.get("RM_KEEP_HTML"): os.remove(hp)
    print(f"stops: {len(NUMS)} tracks ({len(F_SET)} Full, {len(E_SET)} Essential, {len(H_SET)} Highlights, {len(CRA)} Cuarto Real Alto Extras)")
    print("OK ->", OUT_PDF, len(pages), "pages")

build()
