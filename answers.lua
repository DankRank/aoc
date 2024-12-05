function fontdraw(s, alpha, lines, add_space_at_end)
	local o = ""
	for _, line in ipairs(lines) do
		for i = 1, #s do
			o = o .. line[alpha:find(s:sub(i,i), 1, true)]
		end
		if not add_space_at_end and s:sub(-1, -1) ~= "Y" then
			o = o:sub(1, -2)
		end
		o = o .. "\n"
	end
	return o:sub(1, -2)
end
function font6(s, add_space_at_end)
	local alpha = "ABCEFGHIJKLOPRSUYZ"
	local lines = {
		{" ##  ","###  "," ##  ","#### ","#### "," ##  ","#  # "," ### ","  ## ","#  # ","#    "," ##  ","###  ","###  "," ### ","#  # ","#   #","#### "},
		{"#  # ","#  # ","#  # ","#    ","#    ","#  # ","#  # ","  #  ","   # ","# #  ","#    ","#  # ","#  # ","#  # ","#    ","#  # ","#   #","   # "},
		{"#  # ","###  ","#    ","###  ","###  ","#    ","#### ","  #  ","   # ","##   ","#    ","#  # ","#  # ","#  # ","#    ","#  # "," # # ","  #  "},
		{"#### ","#  # ","#    ","#    ","#    ","# ## ","#  # ","  #  ","   # ","# #  ","#    ","#  # ","###  ","###  "," ##  ","#  # ","  #  "," #   "},
		{"#  # ","#  # ","#  # ","#    ","#    ","#  # ","#  # ","  #  ","#  # ","# #  ","#    ","#  # ","#    ","# #  ","   # ","#  # ","  #  ","#    "},
		{"#  # ","###  "," ##  ","#### ","#    "," ### ","#  # "," ### "," ##  ","#  # ","#### "," ##  ","#    ","#  # ","###  "," ##  ","  #  ","#### "},
	}
	return fontdraw(s, alpha, lines, add_space_at_end)
end
function font10(s, add_space_at_end)
	local alpha = "ABCEFGHJKLNPRXZ"
	local lines = {
		{"  ##   ","#####  "," ####  ","###### ","###### "," ####  ","#    # ","   ### ","#    # ","#      ","#    # ","#####  ","#####  ","#    # ","###### "},
		{" #  #  ","#    # ","#    # ","#      ","#      ","#    # ","#    # ","    #  ","#   #  ","#      ","##   # ","#    # ","#    # ","#    # ","     # "},
		{"#    # ","#    # ","#      ","#      ","#      ","#      ","#    # ","    #  ","#  #   ","#      ","##   # ","#    # ","#    # "," #  #  ","     # "},
		{"#    # ","#    # ","#      ","#      ","#      ","#      ","#    # ","    #  ","# #    ","#      ","# #  # ","#    # ","#    # "," #  #  ","    #  "},
		{"#    # ","#####  ","#      ","#####  ","#####  ","#      ","###### ","    #  ","##     ","#      ","# #  # ","#####  ","#####  ","  ##   ","   #   "},
		{"###### ","#    # ","#      ","#      ","#      ","#  ### ","#    # ","    #  ","##     ","#      ","#  # # ","#      ","#  #   ","  ##   ","  #    "},
		{"#    # ","#    # ","#      ","#      ","#      ","#    # ","#    # ","    #  ","# #    ","#      ","#  # # ","#      ","#   #  "," #  #  "," #     "},
		{"#    # ","#    # ","#      ","#      ","#      ","#    # ","#    # ","#   #  ","#  #   ","#      ","#   ## ","#      ","#   #  "," #  #  ","#      "},
		{"#    # ","#    # ","#    # ","#      ","#      ","#   ## ","#    # ","#   #  ","#   #  ","#      ","#   ## ","#      ","#    # ","#    # ","#      "},
		{"#    # ","#####  "," ####  ","###### ","#      "," ### # ","#    # "," ###   ","#    # ","###### ","#    # ","#      ","#    # ","#    # ","###### "},
	}
	return fontdraw(s, alpha, lines, add_space_at_end)
end
return {
	["2015/01/part1"] = "280",
	["2015/01/part2"] = "1797",
	["2015/02/part1"] = "1606483",
	["2015/02/part2"] = "3842356",
	["2015/03/part1"] = "2592",
	["2015/03/part2"] = "2360",
	["2015/04/part1"] = "117946",
	["2015/04/part2"] = "3938038",
	["2015/05/part1"] = "258",
	["2015/05/part2"] = "53",
	["2015/06/part1"] = "377891",
	["2015/06/part2"] = "14110788",
	["2015/07/part1"] = "3176",
	["2015/07/part2"] = "14710",
	["2015/08/part1"] = "1333",
	["2015/08/part2"] = "2046",
	["2015/09/part1"] = "117",
	["2015/09/part2"] = "909",
	["2015/10/part1"] = "360154",
	["2015/10/part2"] = "5103798",
	["2015/11/part1"] = "vzbxxyzz",
	["2015/11/part2"] = "vzcaabcc",
	["2015/12/part1"] = "119433",
	["2015/12/part2"] = "68466",
	["2015/13/part1"] = "733",
	["2015/13/part2"] = "725",
	["2015/14/part1"] = "2640",
	["2015/14/part2"] = "1102",
	["2015/15/part1"] = "222870",
	["2015/15/part2"] = "117936",
	["2015/16/part1"] = "373",
	["2015/16/part2"] = "260",
	["2015/17/part1"] = "4372",
	["2015/17/part2"] = "4",
	["2015/18/part1"] = "1061",
	["2015/18/part2"] = "1006",
	["2015/19/part1"] = "509",
	["2015/19/part2"] = "195",
	["2015/20/part1"] = "665280",
	["2015/20/part2"] = "705600",
	["2015/21/part1"] = "111",
	["2015/21/part2"] = "188",
	["2015/22/part1"] = "900",
	["2015/22/part2"] = "1216",
	["2015/23/part1"] = "170",
	["2015/23/part2"] = "247",
	["2015/24/part1"] = "11846773891",
	["2015/24/part2"] = "80393059",
	["2015/25/part1"] = "19980801",
	["2016/01/part1"] = "243",
	["2016/01/part2"] = "142",
	["2016/02/part1"] = "92435",
	["2016/02/part2"] = "C1A88",
	["2016/03/part1"] = "917",
	["2016/03/part2"] = "1649",
	["2016/04/part1"] = "137896",
	["2016/04/part2"] = "501",
	["2016/05/part1"] = "1a3099aa",
	["2016/05/part2"] = "694190cd",
	["2016/06/part1"] = "gebzfnbt",
	["2016/06/part2"] = "fykjtwyn",
	["2016/07/part1"] = "110",
	["2016/07/part2"] = "242",
	["2016/08/part1"] = "128",
	["2016/08/part2"] = font6("EOARGPHYAO", true),
	["2016/09/part1"] = "120765",
	["2016/09/part2"] = "11658395076",
	["2016/10/part1"] = "86",
	["2016/10/part2"] = "22847",
	["2016/11/part1"] = "31",
	["2016/11/part2"] = "55",
	["2016/12/part1"] = "318009",
	["2016/12/part2"] = "9227663",
	["2016/13/part1"] = "92",
	["2016/13/part2"] = "124",
	["2016/14/part1"] = "18626",
	["2016/14/part2"] = "20092",
	["2016/15/part1"] = "148737",
	["2016/15/part2"] = "2353212",
	["2016/16/part1"] = "10010110010011110",
	["2016/16/part2"] = "01101011101100011",
	["2016/17/part1"] = "DUDDRLRRRD",
	["2016/17/part2"] = "578",
	["2016/18/part1"] = "1974",
	["2016/18/part2"] = "19991126",
	["2016/19/part1"] = "1842613",
	["2016/19/part2"] = "1424135",
	["2016/20/part1"] = "22887907",
	["2016/20/part2"] = "109",
	["2016/21/part1"] = "cbeghdaf",
	["2016/21/part2"] = "bacdefgh",
	["2016/22/part1"] = "950",
	["2016/22/part2"] = "256",
	["2016/23/part1"] = "13958",
	["2016/23/part2"] = "479010518",
	["2016/24/part1"] = "460",
	["2016/24/part2"] = "668",
	["2016/25/part1"] = "198",
	["2017/01/part1"] = nil,
	["2017/01/part2"] = nil,
	["2017/02/part1"] = nil,
	["2017/02/part2"] = nil,
	["2017/03/part1"] = nil,
	["2017/03/part2"] = nil,
	["2017/04/part1"] = nil,
	["2017/04/part2"] = nil,
	["2017/05/part1"] = nil,
	["2017/05/part2"] = nil,
	["2017/06/part1"] = nil,
	["2017/06/part2"] = nil,
	["2017/07/part1"] = nil,
	["2017/07/part2"] = nil,
	["2017/08/part1"] = nil,
	["2017/08/part2"] = nil,
	["2017/09/part1"] = nil,
	["2017/09/part2"] = nil,
	["2017/10/part1"] = nil,
	["2017/10/part2"] = nil,
	["2017/11/part1"] = nil,
	["2017/11/part2"] = nil,
	["2017/12/part1"] = nil,
	["2017/12/part2"] = nil,
	["2017/13/part1"] = nil,
	["2017/13/part2"] = nil,
	["2017/14/part1"] = nil,
	["2017/14/part2"] = nil,
	["2017/15/part1"] = nil,
	["2017/15/part2"] = nil,
	["2017/16/part1"] = nil,
	["2017/16/part2"] = nil,
	["2017/17/part1"] = nil,
	["2017/17/part2"] = nil,
	["2017/18/part1"] = nil,
	["2017/18/part2"] = nil,
	["2017/19/part1"] = nil,
	["2017/19/part2"] = nil,
	["2017/20/part1"] = nil,
	["2017/20/part2"] = nil,
	["2017/21/part1"] = nil,
	["2017/21/part2"] = nil,
	["2017/22/part1"] = nil,
	["2017/22/part2"] = nil,
	["2017/23/part1"] = nil,
	["2017/23/part2"] = nil,
	["2017/24/part1"] = nil,
	["2017/24/part2"] = nil,
	["2017/25/part1"] = nil,
	["2018/01/part1"] = nil,
	["2018/01/part2"] = nil,
	["2018/02/part1"] = nil,
	["2018/02/part2"] = nil,
	["2018/03/part1"] = nil,
	["2018/03/part2"] = nil,
	["2018/04/part1"] = nil,
	["2018/04/part2"] = nil,
	["2018/05/part1"] = nil,
	["2018/05/part2"] = nil,
	["2018/06/part1"] = nil,
	["2018/06/part2"] = nil,
	["2018/07/part1"] = nil,
	["2018/07/part2"] = nil,
	["2018/08/part1"] = nil,
	["2018/08/part2"] = nil,
	["2018/09/part1"] = nil,
	["2018/09/part2"] = nil,
	["2018/10/part1"] = nil,
	["2018/10/part2"] = nil,
	["2018/11/part1"] = nil,
	["2018/11/part2"] = nil,
	["2018/12/part1"] = nil,
	["2018/12/part2"] = nil,
	["2018/13/part1"] = nil,
	["2018/13/part2"] = nil,
	["2018/14/part1"] = nil,
	["2018/14/part2"] = nil,
	["2018/15/part1"] = nil,
	["2018/15/part2"] = nil,
	["2018/16/part1"] = nil,
	["2018/16/part2"] = nil,
	["2018/17/part1"] = nil,
	["2018/17/part2"] = nil,
	["2018/18/part1"] = nil,
	["2018/18/part2"] = nil,
	["2018/19/part1"] = nil,
	["2018/19/part2"] = nil,
	["2018/20/part1"] = nil,
	["2018/20/part2"] = nil,
	["2018/21/part1"] = nil,
	["2018/21/part2"] = nil,
	["2018/22/part1"] = nil,
	["2018/22/part2"] = nil,
	["2018/23/part1"] = nil,
	["2018/23/part2"] = nil,
	["2018/24/part1"] = nil,
	["2018/24/part2"] = nil,
	["2018/25/part1"] = nil,
	["2019/01/part1"] = "3363033",
	["2019/01/part2"] = "5041680",
	["2019/02/part1"] = "3706713",
	["2019/02/part2"] = "8609",
	["2019/03/part1"] = "258",
	["2019/03/part2"] = "12304",
	["2019/04/part1"] = "1019",
	["2019/04/part2"] = "660",
	["2019/05/part1"] = "15508323",
	["2019/05/part2"] = "9006327",
	["2019/06/part1"] = "314702",
	["2019/06/part2"] = "439",
	["2019/07/part1"] = "255840",
	["2019/07/part2"] = "84088865",
	["2019/08/part1"] = "1848",
	["2019/08/part2"] = font6("FGJUZ", true),
	["2019/09/part1"] = "2682107844",
	["2019/09/part2"] = "34738",
	["2019/10/part1"] = "309",
	["2019/10/part2"] = "416",
	["2019/11/part1"] = "1876",
	["2019/11/part2"] = font6("CGPJCGCL"),
	["2019/12/part1"] = "7077",
	["2019/12/part2"] = "402951477454512",
	["2019/13/part1"] = "357",
	["2019/13/part2"] = "17468",
	["2019/14/part1"] = "431448",
	["2019/14/part2"] = "3279311",
	["2019/15/part1"] = "308",
	["2019/15/part2"] = "328",
	["2019/16/part1"] = "42205986",
	["2019/16/part2"] = "13270205",
	["2019/17/part1"] = "3292",
	["2019/17/part2"] = "651043",
	["2019/18/part1"] = "4590",
	["2019/18/part2"] = "2086",
	["2019/19/part1"] = "121",
	["2019/19/part2"] = "15090773",
	["2019/20/part1"] = "666",
	["2019/20/part2"] = "7568",
	["2019/21/part1"] = "19353692",
	["2019/21/part2"] = "1142048514",
	["2019/22/part1"] = "7096",
	["2019/22/part2"] = "27697279941366",
	["2019/23/part1"] = "23954",
	["2019/23/part2"] = "17265",
	["2019/24/part1"] = "27777901",
	["2019/24/part2"] = "2047",
	["2019/25/part1"] = "1073874948",
	["2020/01/part1"] = "972576",
	["2020/01/part2"] = "199300880",
	["2020/02/part1"] = "378",
	["2020/02/part2"] = "280",
	["2020/03/part1"] = "232",
	["2020/03/part2"] = "3952291680",
	["2020/04/part1"] = "226",
	["2020/04/part2"] = "160",
	["2020/05/part1"] = "996",
	["2020/05/part2"] = "671",
	["2020/06/part1"] = "6630",
	["2020/06/part2"] = "3437",
	["2020/07/part1"] = "161",
	["2020/07/part2"] = "30899",
	["2020/08/part1"] = "1586",
	["2020/08/part2"] = "703",
	["2020/09/part1"] = "70639851",
	["2020/09/part2"] = "8249240",
	["2020/10/part1"] = "1917",
	["2020/10/part2"] = "113387824750592",
	["2020/11/part1"] = "2093",
	["2020/11/part2"] = "1862",
	["2020/12/part1"] = "508",
	["2020/12/part2"] = "30761",
	["2020/13/part1"] = "2045",
	["2020/13/part2"] = "402251700208309",
	["2020/14/part1"] = "9628746976360",
	["2020/14/part2"] = "4574598714592",
	["2020/15/part1"] = "620",
	["2020/15/part2"] = "110871",
	["2020/16/part1"] = "21996",
	["2020/16/part2"] = "650080463519",
	["2020/17/part1"] = "271",
	["2020/17/part2"] = "2064",
	["2020/18/part1"] = "3348222486398",
	["2020/18/part2"] = "43423343619505",
	["2020/19/part1"] = "147",
	["2020/19/part2"] = "263",
	["2020/20/part1"] = "47213728755493",
	["2020/20/part2"] = "1599",
	["2020/21/part1"] = "2584",
	["2020/21/part2"] = "fqhpsl,zxncg,clzpsl,zbbnj,jkgbvlxh,dzqc,ppj,glzb",
	["2020/22/part1"] = "32472",
	["2020/22/part2"] = "36463",
	["2020/23/part1"] = "78569234",
	["2020/23/part2"] = "565615814504",
	["2020/24/part1"] = "332",
	["2020/24/part2"] = "3900",
	["2020/25/part1"] = "6421487",
	["2021/01/part1"] = "1581",
	["2021/01/part2"] = "1618",
	["2021/02/part1"] = "1924923",
	["2021/02/part2"] = "1982495697",
	["2021/03/part1"] = "2583164",
	["2021/03/part2"] = "2784375",
	["2021/04/part1"] = "41503",
	["2021/04/part2"] = "3178",
	["2021/05/part1"] = "5774",
	["2021/05/part2"] = "18423",
	["2021/06/part1"] = "391671",
	["2021/06/part2"] = "1754000560399",
	["2021/07/part1"] = "340987",
	["2021/07/part2"] = "96987874",
	["2021/08/part1"] = "409",
	["2021/08/part2"] = "1024649",
	["2021/09/part1"] = "603",
	["2021/09/part2"] = "786780",
	["2021/10/part1"] = "399153",
	["2021/10/part2"] = "2995077699",
	["2021/11/part1"] = "1688",
	["2021/11/part2"] = "403",
	["2021/12/part1"] = "4413",
	["2021/12/part2"] = "118803",
	["2021/13/part1"] = "765",
	["2021/13/part2"] = font6("RZKZLPGH"),
	["2021/14/part1"] = "2587",
	["2021/14/part2"] = "3318837563123",
	["2021/15/part1"] = "458",
	["2021/15/part2"] = "2800",
	["2021/16/part1"] = "901",
	["2021/16/part2"] = "110434737925",
	["2021/17/part1"] = "9180",
	["2021/17/part2"] = "3767",
	["2021/18/part1"] = "3734",
	["2021/18/part2"] = "4837",
	["2021/19/part1"] = "381",
	["2021/19/part2"] = "12201",
	["2021/20/part1"] = "5432",
	["2021/20/part2"] = "16016",
	["2021/21/part1"] = "908091",
	["2021/21/part2"] = "190897246590017",
	["2021/22/part1"] = "596598",
	["2021/22/part2"] = "1199121349148621",
	["2021/23/part1"] = "17400",
	["2021/23/part2"] = "46120",
	["2021/24/part1"] = "99196997985942",
	["2021/24/part2"] = "84191521311611",
	["2021/25/part1"] = "278",
	["2022/01/part1"] = "72602",
	["2022/01/part2"] = "207410",
	["2022/02/part1"] = "12794",
	["2022/02/part2"] = "14979",
	["2022/03/part1"] = "8105",
	["2022/03/part2"] = "2363",
	["2022/04/part1"] = "483",
	["2022/04/part2"] = "874",
	["2022/05/part1"] = "FWNSHLDNZ",
	["2022/05/part2"] = "RNRGDNFQG",
	["2022/06/part1"] = "1300",
	["2022/06/part2"] = "3986",
	["2022/07/part1"] = "1447046",
	["2022/07/part2"] = "578710",
	["2022/08/part1"] = "1835",
	["2022/08/part2"] = "263670",
	["2022/09/part1"] = "6243",
	["2022/09/part2"] = "2630",
	["2022/10/part1"] = "12540",
	["2022/10/part2"] = font6("FECZELHE", true),
	["2022/11/part1"] = "54253",
	["2022/11/part2"] = "13119526120",
	["2022/12/part1"] = "394",
	["2022/12/part2"] = "388",
	["2022/13/part1"] = "6272",
	["2022/13/part2"] = "22288",
	["2022/14/part1"] = "799",
	["2022/14/part2"] = "29076",
	["2022/15/part1"] = "5607466",
	["2022/15/part2"] = "12543202766584",
	["2022/16/part1"] = "1850",
	["2022/16/part2"] = "2306",
	["2022/17/part1"] = "3211",
	["2022/17/part2"] = "1589142857183",
	["2022/18/part1"] = "3346",
	["2022/18/part2"] = "1980",
	["2022/19/part1"] = "1725",
	["2022/19/part2"] = "15510",
	["2022/20/part1"] = "7225",
	["2022/20/part2"] = "548634267428",
	["2022/21/part1"] = "38914458159166",
	["2022/21/part2"] = "3665520865940",
	["2022/22/part1"] = "181128",
	["2022/22/part2"] = "52311",
	["2022/23/part1"] = "3996",
	["2022/23/part2"] = "908",
	["2022/24/part1"] = "230",
	["2022/24/part2"] = "713",
	["2022/25/part1"] = "20===-20-020=0001-02",
	["2023/01/part1"] = "54605",
	["2023/01/part2"] = "55429",
	["2023/02/part1"] = "2447",
	["2023/02/part2"] = "56322",
	["2023/03/part1"] = "521601",
	["2023/03/part2"] = "80694070",
	["2023/04/part1"] = "23028",
	["2023/04/part2"] = "9236992",
	["2023/05/part1"] = "324724204",
	["2023/05/part2"] = "104070862",
	["2023/06/part1"] = "6209190",
	["2023/06/part2"] = "28545089",
	["2023/07/part1"] = "250453939",
	["2023/07/part2"] = "248652697",
	["2023/08/part1"] = "18827",
	["2023/08/part2"] = "20220305520997",
	["2023/09/part1"] = "1916822650",
	["2023/09/part2"] = "966",
	["2023/10/part1"] = "6714",
	["2023/10/part2"] = "429",
	["2023/11/part1"] = "9623138",
	["2023/11/part2"] = "726820169514",
	["2023/12/part1"] = "8075",
	["2023/12/part2"] = "4232520187524",
	["2023/13/part1"] = "37561",
	["2023/13/part2"] = "31108",
	["2023/14/part1"] = "111979",
	["2023/14/part2"] = "102055",
	["2023/15/part1"] = "495972",
	["2023/15/part2"] = "245223",
	["2023/16/part1"] = "6883",
	["2023/16/part2"] = "7228",
	["2023/17/part1"] = "1260",
	["2023/17/part2"] = "1416",
	["2023/18/part1"] = "70253",
	["2023/18/part2"] = "131265059885080",
	["2023/19/part1"] = "472630",
	["2023/19/part2"] = "116738260946855",
	["2023/20/part1"] = "867118762",
	["2023/20/part2"] = "217317393039529",
	["2023/21/part1"] = "3709",
	["2023/21/part2"] = "617361073602319",
	["2023/22/part1"] = "418",
	["2023/22/part2"] = "70702",
	["2023/23/part1"] = "2254",
	["2023/23/part2"] = "6394",
	["2023/24/part1"] = "12015",
	["2023/24/part2"] = "1016365642179116",
	["2023/25/part1"] = "598120",
	["2024/01/part1"] = "2430334",
	["2024/01/part2"] = "28786472",
	["2024/02/part1"] = "236",
	["2024/02/part2"] = "308",
	["2024/03/part1"] = "164730528",
	["2024/03/part2"] = "70478672",
	["2024/04/part1"] = "2557",
	["2024/04/part2"] = "1854",
	["2024/05/part1"] = "6051",
	["2024/05/part2"] = "5093",
	["2024/06/part1"] = nil,
	["2024/06/part2"] = nil,
	["2024/07/part1"] = nil,
	["2024/07/part2"] = nil,
	["2024/08/part1"] = nil,
	["2024/08/part2"] = nil,
	["2024/09/part1"] = nil,
	["2024/09/part2"] = nil,
	["2024/10/part1"] = nil,
	["2024/10/part2"] = nil,
	["2024/11/part1"] = nil,
	["2024/11/part2"] = nil,
	["2024/12/part1"] = nil,
	["2024/12/part2"] = nil,
	["2024/13/part1"] = nil,
	["2024/13/part2"] = nil,
	["2024/14/part1"] = nil,
	["2024/14/part2"] = nil,
	["2024/15/part1"] = nil,
	["2024/15/part2"] = nil,
	["2024/16/part1"] = nil,
	["2024/16/part2"] = nil,
	["2024/17/part1"] = nil,
	["2024/17/part2"] = nil,
	["2024/18/part1"] = nil,
	["2024/18/part2"] = nil,
	["2024/19/part1"] = nil,
	["2024/19/part2"] = nil,
	["2024/20/part1"] = nil,
	["2024/20/part2"] = nil,
	["2024/21/part1"] = nil,
	["2024/21/part2"] = nil,
	["2024/22/part1"] = nil,
	["2024/22/part2"] = nil,
	["2024/23/part1"] = nil,
	["2024/23/part2"] = nil,
	["2024/24/part1"] = nil,
	["2024/24/part2"] = nil,
	["2024/25/part1"] = nil,
}
