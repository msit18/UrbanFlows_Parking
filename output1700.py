import numpy as np

Array = [
[['1700002475.jpg'], 0.0000001, 0.98568117618560791, 28.0, 419.0, 240.0, 538.0, 0.0000001, 0.9786829948425293, 735.0, 445.0, 963.0, 543.0, 0.0000001, 0.96584498882293701, 1365.0, 449.0, 1541.0, 560.0, 0.0000001, 0.90339386463165283, 321.0, 419.0, 608.0, 539.0],
[['1700004950.jpg'], 0.0000001, 0.98575365543365479, 30.0, 419.0, 238.0, 538.0, 0.0000001, 0.97036260366439819, 730.0, 444.0, 964.0, 542.0, 0.0000001, 0.92554616928100586, 326.0, 422.0, 610.0, 539.0, 0.0000001, 0.78404343128204346, 675.0, 451.0, 789.0, 523.0],
[['1700013050.jpg'], 0.0000001, 0.98766040802001953, 29.0, 419.0, 238.0, 537.0, 0.0000001, 0.98115414381027222, 690.0, 444.0, 966.0, 544.0, 0.0000001, 0.89625853300094604, 324.0, 418.0, 611.0, 539.0],
[['1700007875.jpg'], 0.0000001, 0.98659348487854004, 29.0, 418.0, 236.0, 538.0, 0.0000001, 0.97779262065887451, 695.0, 444.0, 964.0, 543.0, 0.0000001, 0.84018474817276001, 322.0, 420.0, 614.0, 539.0],
[['1700007200.jpg'], 0.0000001, 0.98643594980239868, 34.0, 419.0, 234.0, 531.0, 0.0000001, 0.98055756092071533, 687.0, 445.0, 964.0, 544.0, 0.0000001, 0.92565768957138062, 330.0, 421.0, 610.0, 539.0],
[['1700009675.jpg'], 0.0000001, 0.98824292421340942, 33.0, 420.0, 235.0, 528.0, 0.0000001, 0.98473048210144043, 691.0, 444.0, 965.0, 543.0, 0.0000001, 0.98066985607147217, 1402.0, 507.0, 1574.0, 609.0, 0.0000001, 0.94731926918029785, 324.0, 419.0, 610.0, 540.0],
[['1700010350.jpg'], 0.0000001, 0.98623102903366089, 32.0, 419.0, 239.0, 531.0, 0.0000001, 0.98490208387374878, 684.0, 443.0, 965.0, 543.0, 0.0000001, 0.84475594758987427, 330.0, 418.0, 609.0, 540.0],
[['1700009900.jpg'], 0.0000001, 0.984416663646698, 36.0, 419.0, 239.0, 536.0, 0.0000001, 0.9801943302154541, 689.0, 444.0, 966.0, 543.0, 0.0000001, 0.9266211986541748, 325.0, 419.0, 612.0, 539.0],
[['1700012375.jpg'], 0.0000001, 0.98828226327896118, 30.0, 419.0, 236.0, 535.0, 0.0000001, 0.97609794139862061, 688.0, 444.0, 963.0, 543.0, 0.0000001, 0.85166561603546143, 323.0, 421.0, 608.0, 540.0],
[['1700013275.jpg'], 0.0000001, 0.98266887664794922, 701.0, 444.0, 966.0, 542.0, 0.0000001, 0.96660721302032471, 512.0, 418.0, 638.0, 540.0, 0.0000002, 0.99435389041900635, 13.0, 375.0, 506.0, 662.0],
[['1700005625.jpg'], 0.0000001, 0.98759913444519043, 30.0, 419.0, 238.0, 534.0, 0.0000001, 0.97883087396621704, 697.0, 445.0, 964.0, 543.0, 0.0000001, 0.87672668695449829, 327.0, 421.0, 606.0, 541.0],
[['1700006075.jpg'], 0.0000001, 0.98208057880401611, 31.0, 418.0, 236.0, 532.0, 0.0000001, 0.97736674547195435, 699.0, 444.0, 965.0, 542.0, 0.0000001, 0.9195559024810791, 322.0, 421.0, 606.0, 539.0],
[['1700009225.jpg'], 0.0000001, 0.98974823951721191, 30.0, 418.0, 237.0, 536.0, 0.0000001, 0.98432826995849609, 696.0, 443.0, 964.0, 543.0, 0.0000001, 0.92995285987854004, 328.0, 419.0, 612.0, 540.0],
[['1700009450.jpg'], 0.0000001, 0.98927021026611328, 34.0, 419.0, 237.0, 531.0, 0.0000001, 0.97601455450057983, 689.0, 443.0, 966.0, 543.0, 0.0000001, 0.92226439714431763, 325.0, 420.0, 612.0, 539.0],
[['1700004500.jpg'], 0.0000001, 0.98643481731414795, 29.0, 419.0, 238.0, 531.0, 0.0000001, 0.9851948618888855, 717.0, 445.0, 965.0, 544.0, 0.0000001, 0.8906024694442749, 326.0, 422.0, 607.0, 540.0],
[['1700001350.jpg'], 0.0000001, 0.99777776002883911, 748.0, 451.0, 1019.0, 613.0, 0.0000001, 0.98195952177047729, 31.0, 420.0, 234.0, 530.0, 0.0000001, 0.9050026535987854, 325.0, 421.0, 609.0, 540.0, 0.0000001, 0.84495025873184204, 1504.0, 567.0, 1596.0, 654.0],
[['1700001800.jpg'], 0.0000001, 0.99294561147689819, 812.0, 445.0, 1079.0, 543.0, 0.0000001, 0.98626536130905151, 35.0, 419.0, 240.0, 530.0, 0.0000001, 0.91310369968414307, 332.0, 420.0, 609.0, 539.0],
[['1700000675.jpg'], 0.0000001, 0.98813241720199585, 32.0, 419.0, 238.0, 531.0, 0.0000001, 0.93088346719741821, 326.0, 420.0, 610.0, 539.0],
[['1700008550.jpg'], 0.0000001, 0.99553900957107544, 234.0, 490.0, 517.0, 625.0, 0.0000001, 0.99326020479202271, 898.0, 511.0, 1207.0, 639.0, 0.0000001, 0.9779125452041626, 29.0, 420.0, 239.0, 530.0, 0.0000001, 0.97573065757751465, 694.0, 445.0, 976.0, 541.0, 0.0000001, 0.92932158708572388, 386.0, 422.0, 610.0, 540.0],
[['1700003825.jpg'], 0.0000001, 0.99652343988418579, 1379.0, 585.0, 1584.0, 704.0, 0.0000001, 0.99025946855545044, 588.0, 480.0, 940.0, 630.0, 0.0000001, 0.98244470357894897, 31.0, 419.0, 240.0, 535.0, 0.0000001, 0.94039547443389893, 333.0, 423.0, 609.0, 540.0, 0.0000001, 0.92617636919021606, 1372.0, 448.0, 1531.0, 532.0, 0.0000001, 0.88852518796920776, 729.0, 432.0, 968.0, 565.0],
[['1700003375.jpg'], 0.0000001, 0.98723119497299194, 32.0, 419.0, 238.0, 534.0, 0.0000001, 0.98441952466964722, 685.0, 443.0, 964.0, 542.0, 0.0000001, 0.90143394470214844, 322.0, 422.0, 611.0, 540.0],
[['1700002700.jpg'], 0.0000001, 0.9923592209815979, 1368.0, 451.0, 1543.0, 551.0, 0.0000001, 0.98095118999481201, 716.0, 445.0, 962.0, 544.0, 0.0000001, 0.97178244590759277, 31.0, 418.0, 237.0, 534.0, 0.0000001, 0.87858641147613525, 333.0, 421.0, 606.0, 540.0],
[['1700012825.jpg'], 0.0000001, 0.98715579509735107, 32.0, 419.0, 239.0, 536.0, 0.0000001, 0.97810167074203491, 687.0, 443.0, 963.0, 543.0, 0.0000001, 0.91563475131988525, 320.0, 419.0, 608.0, 539.0],
[['1700003150.jpg'], 0.0000001, 0.98511523008346558, 31.0, 419.0, 241.0, 533.0, 0.0000001, 0.97855567932128906, 695.0, 443.0, 965.0, 542.0, 0.0000001, 0.92563581466674805, 326.0, 421.0, 604.0, 539.0],
[['1700011025.jpg'], 0.0000001, 0.99537259340286255, 1230.0, 446.0, 1444.0, 566.0, 0.0000001, 0.98897832632064819, 27.0, 420.0, 239.0, 527.0, 0.0000001, 0.98043513298034668, 685.0, 443.0, 967.0, 543.0, 0.0000001, 0.91369932889938354, 327.0, 421.0, 610.0, 539.0],
[['1700009000.jpg'], 0.0000001, 0.99230897426605225, 28.0, 418.0, 238.0, 536.0, 0.0000001, 0.97980117797851562, 691.0, 444.0, 966.0, 543.0, 0.0000001, 0.96641069650650024, 328.0, 421.0, 609.0, 540.0],
[['1700010800.jpg'], 0.0000001, 0.98980975151062012, 400.0, 482.0, 755.0, 635.0, 0.0000001, 0.98579514026641846, 30.0, 419.0, 237.0, 534.0, 0.0000001, 0.98128616809844971, 738.0, 619.0, 1118.0, 756.0, 0.0000001, 0.95608842372894287, 748.0, 443.0, 964.0, 543.0, 0.0000001, 0.88537263870239258, 325.0, 420.0, 612.0, 537.0],
[['1700005850.jpg'], 0.0000001, 0.98682934045791626, 34.0, 418.0, 240.0, 535.0, 0.0000001, 0.97877776622772217, 702.0, 445.0, 962.0, 544.0, 0.0000001, 0.91873687505722046, 339.0, 420.0, 609.0, 540.0],
[['1700011475.jpg'], 0.0000001, 0.98469191789627075, 29.0, 418.0, 240.0, 531.0, 0.0000001, 0.97601419687271118, 685.0, 443.0, 968.0, 544.0, 0.0000001, 0.93199878931045532, 325.0, 421.0, 607.0, 539.0, 0.0000001, 0.71733355522155762, 694.0, 645.0, 1181.0, 756.0],
[['1700001125.jpg'], 0.0000001, 0.99104708433151245, 34.0, 421.0, 237.0, 529.0, 0.0000001, 0.97828924655914307, 1161.0, 526.0, 1396.0, 686.0, 0.0000001, 0.93985444307327271, 324.0, 420.0, 607.0, 540.0],
[['1700004275.jpg'], 0.0000001, 0.98745626211166382, 30.0, 420.0, 242.0, 530.0, 0.0000001, 0.98614174127578735, 1371.0, 447.0, 1537.0, 534.0, 0.0000001, 0.98060846328735352, 696.0, 443.0, 966.0, 543.0, 0.0000001, 0.8994099497795105, 324.0, 423.0, 610.0, 540.0],
[['1700008325.jpg'], 0.0000001, 0.97973883152008057, 37.0, 418.0, 240.0, 536.0, 0.0000001, 0.97603338956832886, 701.0, 445.0, 965.0, 543.0, 0.0000001, 0.96698057651519775, 1135.0, 603.0, 1433.0, 728.0, 0.0000001, 0.94981300830841064, 328.0, 420.0, 609.0, 539.0],
[['1700005175.jpg'], 0.0000001, 0.9859306812286377, 30.0, 419.0, 237.0, 538.0, 0.0000001, 0.98592698574066162, 505.0, 490.0, 879.0, 637.0, 0.0000001, 0.9333493709564209, 326.0, 421.0, 608.0, 539.0, 0.0000001, 0.92109447717666626, 789.0, 430.0, 963.0, 544.0],
[['1700007650.jpg'], 0.0000001, 0.98983454704284668, 29.0, 419.0, 236.0, 534.0, 0.0000001, 0.97745037078857422, 702.0, 444.0, 968.0, 544.0, 0.0000001, 0.89307910203933716, 324.0, 419.0, 608.0, 540.0],
[['1700006975.jpg'], 0.0000001, 0.99097096920013428, 28.0, 419.0, 237.0, 538.0, 0.0000001, 0.97951561212539673, 705.0, 443.0, 965.0, 542.0, 0.0000001, 0.94578844308853149, 327.0, 423.0, 609.0, 538.0],
[['1700000900.jpg'], 0.0000001, 0.99444961547851562, 1329.0, 488.0, 1522.0, 604.0, 0.0000001, 0.98626166582107544, 31.0, 419.0, 239.0, 532.0, 0.0000001, 0.94972419738769531, 329.0, 420.0, 608.0, 540.0],
[['1700008775.jpg'], 0.0000001, 0.99047559499740601, 34.0, 419.0, 238.0, 533.0, 0.0000001, 0.98412251472473145, 689.0, 443.0, 967.0, 543.0, 0.0000001, 0.93513697385787964, 331.0, 420.0, 609.0, 538.0],
[['1700002925.jpg'], 0.0000001, 0.99392735958099365, 1257.0, 480.0, 1565.0, 666.0, 0.0000001, 0.98675143718719482, 30.0, 419.0, 239.0, 532.0, 0.0000001, 0.97892773151397705, 696.0, 444.0, 963.0, 543.0, 0.0000001, 0.90026217699050903, 323.0, 421.0, 609.0, 538.0],
[['1700002025.jpg'], 0.0000001, 0.99389076232910156, 168.0, 578.0, 637.0, 760.0, 0.0000001, 0.97953641414642334, 683.0, 442.0, 964.0, 542.0, 0.0000001, 0.97620570659637451, 31.0, 418.0, 237.0, 536.0, 0.0000001, 0.92109960317611694, 329.0, 422.0, 608.0, 539.0],
[['1700012150.jpg'], 0.0000001, 0.98103147745132446, 685.0, 444.0, 963.0, 544.0, 0.0000001, 0.97868722677230835, 31.0, 420.0, 238.0, 535.0, 0.0000001, 0.91924470663070679, 329.0, 423.0, 608.0, 537.0, 0.0000001, 0.90976208448410034, 170.0, 505.0, 507.0, 637.0],
[['1700010125.jpg'], 0.0000001, 0.99023729562759399, 35.0, 418.0, 240.0, 532.0, 0.0000001, 0.98557615280151367, 683.0, 441.0, 974.0, 542.0, 0.0000001, 0.91603231430053711, 325.0, 417.0, 612.0, 538.0, 0.0000002, 0.86336463689804077, 1081.0, 362.0, 1559.0, 655.0],
[['1700004050.jpg'], 0.0000001, 0.98280173540115356, 694.0, 445.0, 966.0, 543.0, 0.0000001, 0.98221015930175781, 31.0, 419.0, 239.0, 535.0, 0.0000001, 0.89119517803192139, 328.0, 420.0, 609.0, 539.0],
[['1700006300.jpg'], 0.0000001, 0.99300026893615723, 156.0, 563.0, 592.0, 706.0, 0.0000001, 0.98553407192230225, 28.0, 419.0, 236.0, 531.0, 0.0000001, 0.98042106628417969, 700.0, 446.0, 965.0, 544.0, 0.0000001, 0.924419105052948, 326.0, 422.0, 610.0, 540.0],
[['1700012600.jpg'], 0.0000001, 0.98603188991546631, 689.0, 444.0, 965.0, 544.0, 0.0000001, 0.97895675897598267, 28.0, 418.0, 241.0, 538.0, 0.0000001, 0.91562354564666748, 326.0, 421.0, 610.0, 540.0],
[['1700011700.jpg'], 0.0000001, 0.98874145746231079, 33.0, 419.0, 238.0, 529.0, 0.0000001, 0.97964853048324585, 686.0, 444.0, 966.0, 544.0, 0.0000001, 0.87946832180023193, 324.0, 420.0, 604.0, 539.0],
[['1700002250.jpg'], 0.0000001, 0.98620253801345825, 34.0, 419.0, 239.0, 531.0, 0.0000001, 0.97920036315917969, 722.0, 444.0, 964.0, 544.0, 0.0000001, 0.91193884611129761, 322.0, 420.0, 607.0, 540.0],
[['1700006525.jpg'], 0.0000001, 0.99101734161376953, 593.0, 498.0, 951.0, 640.0, 0.0000001, 0.98531794548034668, 31.0, 418.0, 236.0, 533.0, 0.0000001, 0.9145970344543457, 320.0, 421.0, 609.0, 538.0, 0.0000001, 0.7281111478805542, 724.0, 442.0, 968.0, 523.0],
[['1700003600.jpg'], 0.0000001, 0.99520879983901978, 140.0, 485.0, 468.0, 636.0, 0.0000001, 0.98909133672714233, 1252.0, 448.0, 1417.0, 575.0, 0.0000001, 0.98413115739822388, 714.0, 444.0, 964.0, 543.0, 0.0000001, 0.97404509782791138, 30.0, 419.0, 253.0, 538.0, 0.0000001, 0.97288322448730469, 330.0, 422.0, 610.0, 539.0, 0.0000001, 0.70017874240875244, 676.0, 451.0, 780.0, 528.0],
[['1700007425.jpg'], 0.0000001, 0.98190593719482422, 35.0, 419.0, 237.0, 530.0, 0.0000001, 0.97764068841934204, 700.0, 444.0, 966.0, 543.0, 0.0000001, 0.92037469148635864, 328.0, 422.0, 613.0, 539.0],
[['1700011250.jpg'], 0.0000001, 0.98277443647384644, 30.0, 419.0, 237.0, 533.0, 0.0000001, 0.98089128732681274, 692.0, 444.0, 965.0, 542.0, 0.0000001, 0.92788618803024292, 321.0, 422.0, 609.0, 538.0],
[['1700008100.jpg'], 0.0000001, 0.98330193758010864, 31.0, 419.0, 241.0, 531.0, 0.0000001, 0.98212701082229614, 702.0, 444.0, 965.0, 545.0, 0.0000001, 0.90487366914749146, 327.0, 421.0, 611.0, 540.0],
[['1700000225.jpg'], 0.0000001, 0.98530268669128418, 33.0, 420.0, 240.0, 535.0, 0.0000001, 0.89882099628448486, 321.0, 419.0, 610.0, 540.0],
[['1700011925.jpg'], 0.0000001, 0.98764228820800781, 35.0, 418.0, 241.0, 531.0, 0.0000001, 0.98237383365631104, 690.0, 443.0, 967.0, 542.0, 0.0000001, 0.8989068865776062, 326.0, 422.0, 611.0, 539.0],
[['1700001575.jpg'], 0.0000001, 0.99658280611038208, 846.0, 447.0, 1116.0, 556.0, 0.0000001, 0.98891091346740723, 31.0, 418.0, 241.0, 526.0, 0.0000001, 0.92571896314620972, 323.0, 420.0, 612.0, 540.0],
[['1700006750.jpg'], 0.0000001, 0.98957061767578125, 31.0, 419.0, 240.0, 529.0, 0.0000001, 0.98027598857879639, 703.0, 445.0, 962.0, 543.0, 0.0000001, 0.92619842290878296, 324.0, 420.0, 609.0, 541.0, 0.0000001, 0.70771569013595581, 1508.0, 573.0, 1595.0, 677.0],
[['1700010575.jpg'], 0.0000001, 0.98622328042984009, 34.0, 418.0, 239.0, 529.0, 0.0000001, 0.98031091690063477, 687.0, 444.0, 965.0, 542.0, 0.0000001, 0.92493772506713867, 330.0, 422.0, 611.0, 539.0],
[['1700005400.jpg'], 0.0000001, 0.97941005229949951, 701.0, 444.0, 961.0, 543.0, 0.0000001, 0.96754348278045654, 29.0, 418.0, 233.0, 535.0, 0.0000001, 0.93306738138198853, 327.0, 421.0, 610.0, 540.0],
[['1700000450.jpg'], 0.0000001, 0.98550701141357422, 36.0, 418.0, 240.0, 532.0, 0.0000001, 0.93049782514572144, 323.0, 420.0, 610.0, 540.0, 0.0000001, 0.86527800559997559, 1419.0, 488.0, 1594.0, 595.0],
[['1700004725.jpg'], 0.0000001, 0.98910647630691528, 30.0, 418.0, 236.0, 536.0, 0.0000001, 0.97883599996566772, 702.0, 444.0, 964.0, 543.0, 0.0000001, 0.9412725567817688, 323.0, 420.0, 611.0, 540.0, 0.0000001, 0.93260067701339722, 1099.0, 608.0, 1424.0, 731.0],
[['1700000000.jpg'], 0.0000001, 0.98417246341705322, 27.0, 418.0, 230.0, 532.0, 0.0000001, 0.77678388357162476, 319.0, 420.0, 605.0, 538.0]]


total = [[[27.0, 418.0, 230.0, 532.0], [319.0, 420.0, 605.0, 538.0]], [[33.0, 420.0, 240.0, 535.0], [321.0, 419.0, 610.0, 540.0]], [[36.0, 418.0, 240.0, 532.0], [323.0, 420.0, 610.0, 540.0], [1419.0, 488.0, 1594.0, 595.0]], [[32.0, 419.0, 238.0, 531.0], [326.0, 420.0, 610.0, 539.0]], [[1329.0, 488.0, 1522.0, 604.0], [31.0, 419.0, 239.0, 532.0], [329.0, 420.0, 608.0, 540.0]], [[34.0, 421.0, 237.0, 529.0], [1161.0, 526.0, 1396.0, 686.0], [324.0, 420.0, 607.0, 540.0]], [[748.0, 451.0, 1019.0, 613.0], [31.0, 420.0, 234.0, 530.0], [325.0, 421.0, 609.0, 540.0], [1504.0, 567.0, 1596.0, 654.0]], [[846.0, 447.0, 1116.0, 556.0], [31.0, 418.0, 241.0, 526.0], [323.0, 420.0, 612.0, 540.0]], [[812.0, 445.0, 1079.0, 543.0], [35.0, 419.0, 240.0, 530.0], [332.0, 420.0, 609.0, 539.0]], [[168.0, 578.0, 637.0, 760.0], [683.0, 442.0, 964.0, 542.0], [31.0, 418.0, 237.0, 536.0], [329.0, 422.0, 608.0, 539.0]], [[34.0, 419.0, 239.0, 531.0], [722.0, 444.0, 964.0, 544.0], [322.0, 420.0, 607.0, 540.0]], [[28.0, 419.0, 240.0, 538.0], [735.0, 445.0, 963.0, 543.0], [1365.0, 449.0, 1541.0, 560.0], [321.0, 419.0, 608.0, 539.0]], [[1368.0, 451.0, 1543.0, 551.0], [716.0, 445.0, 962.0, 544.0], [31.0, 418.0, 237.0, 534.0], [333.0, 421.0, 606.0, 540.0]], [[1257.0, 480.0, 1565.0, 666.0], [30.0, 419.0, 239.0, 532.0], [696.0, 444.0, 963.0, 543.0], [323.0, 421.0, 609.0, 538.0]], [[31.0, 419.0, 241.0, 533.0], [695.0, 443.0, 965.0, 542.0], [326.0, 421.0, 604.0, 539.0]], [[32.0, 419.0, 238.0, 534.0], [685.0, 443.0, 964.0, 542.0], [322.0, 422.0, 611.0, 540.0]], [[140.0, 485.0, 468.0, 636.0], [1252.0, 448.0, 1417.0, 575.0], [714.0, 444.0, 964.0, 543.0], [30.0, 419.0, 253.0, 538.0], [330.0, 422.0, 610.0, 539.0], [676.0, 451.0, 780.0, 528.0]], [[1379.0, 585.0, 1584.0, 704.0], [588.0, 480.0, 940.0, 630.0], [31.0, 419.0, 240.0, 535.0], [333.0, 423.0, 609.0, 540.0], [1372.0, 448.0, 1531.0, 532.0], [729.0, 432.0, 968.0, 565.0]], [[694.0, 445.0, 966.0, 543.0], [31.0, 419.0, 239.0, 535.0], [328.0, 420.0, 609.0, 539.0]], [[30.0, 420.0, 242.0, 530.0], [1371.0, 447.0, 1537.0, 534.0], [696.0, 443.0, 966.0, 543.0], [324.0, 423.0, 610.0, 540.0]], [[29.0, 419.0, 238.0, 531.0], [717.0, 445.0, 965.0, 544.0], [326.0, 422.0, 607.0, 540.0]], [[30.0, 418.0, 236.0, 536.0], [702.0, 444.0, 964.0, 543.0], [323.0, 420.0, 611.0, 540.0], [1099.0, 608.0, 1424.0, 731.0]], [[30.0, 419.0, 238.0, 538.0], [730.0, 444.0, 964.0, 542.0], [326.0, 422.0, 610.0, 539.0], [675.0, 451.0, 789.0, 523.0]], [[30.0, 419.0, 237.0, 538.0], [505.0, 490.0, 879.0, 637.0], [326.0, 421.0, 608.0, 539.0], [789.0, 430.0, 963.0, 544.0]], [[701.0, 444.0, 961.0, 543.0], [29.0, 418.0, 233.0, 535.0], [327.0, 421.0, 610.0, 540.0]], [[30.0, 419.0, 238.0, 534.0], [697.0, 445.0, 964.0, 543.0], [327.0, 421.0, 606.0, 541.0]], [[34.0, 418.0, 240.0, 535.0], [702.0, 445.0, 962.0, 544.0], [339.0, 420.0, 609.0, 540.0]], [[31.0, 418.0, 236.0, 532.0], [699.0, 444.0, 965.0, 542.0], [322.0, 421.0, 606.0, 539.0]], [[156.0, 563.0, 592.0, 706.0], [28.0, 419.0, 236.0, 531.0], [700.0, 446.0, 965.0, 544.0], [326.0, 422.0, 610.0, 540.0]], [[593.0, 498.0, 951.0, 640.0], [31.0, 418.0, 236.0, 533.0], [320.0, 421.0, 609.0, 538.0], [724.0, 442.0, 968.0, 523.0]], [[31.0, 419.0, 240.0, 529.0], [703.0, 445.0, 962.0, 543.0], [324.0, 420.0, 609.0, 541.0], [1508.0, 573.0, 1595.0, 677.0]], [[28.0, 419.0, 237.0, 538.0], [705.0, 443.0, 965.0, 542.0], [327.0, 423.0, 609.0, 538.0]], [[34.0, 419.0, 234.0, 531.0], [687.0, 445.0, 964.0, 544.0], [330.0, 421.0, 610.0, 539.0]], [[35.0, 419.0, 237.0, 530.0], [700.0, 444.0, 966.0, 543.0], [328.0, 422.0, 613.0, 539.0]], [[29.0, 419.0, 236.0, 534.0], [702.0, 444.0, 968.0, 544.0], [324.0, 419.0, 608.0, 540.0]], [[29.0, 418.0, 236.0, 538.0], [695.0, 444.0, 964.0, 543.0], [322.0, 420.0, 614.0, 539.0]], [[31.0, 419.0, 241.0, 531.0], [702.0, 444.0, 965.0, 545.0], [327.0, 421.0, 611.0, 540.0]], [[37.0, 418.0, 240.0, 536.0], [701.0, 445.0, 965.0, 543.0], [1135.0, 603.0, 1433.0, 728.0], [328.0, 420.0, 609.0, 539.0]], [[234.0, 490.0, 517.0, 625.0], [898.0, 511.0, 1207.0, 639.0], [29.0, 420.0, 239.0, 530.0], [694.0, 445.0, 976.0, 541.0], [386.0, 422.0, 610.0, 540.0]], [[34.0, 419.0, 238.0, 533.0], [689.0, 443.0, 967.0, 543.0], [331.0, 420.0, 609.0, 538.0]], [[28.0, 418.0, 238.0, 536.0], [691.0, 444.0, 966.0, 543.0], [328.0, 421.0, 609.0, 540.0]], [[30.0, 418.0, 237.0, 536.0], [696.0, 443.0, 964.0, 543.0], [328.0, 419.0, 612.0, 540.0]], [[34.0, 419.0, 237.0, 531.0], [689.0, 443.0, 966.0, 543.0], [325.0, 420.0, 612.0, 539.0]], [[33.0, 420.0, 235.0, 528.0], [691.0, 444.0, 965.0, 543.0], [1402.0, 507.0, 1574.0, 609.0], [324.0, 419.0, 610.0, 540.0]], [[36.0, 419.0, 239.0, 536.0], [689.0, 444.0, 966.0, 543.0], [325.0, 419.0, 612.0, 539.0]], [[35.0, 418.0, 240.0, 532.0], [683.0, 441.0, 974.0, 542.0], [325.0, 417.0, 612.0, 538.0], [1081.0, 362.0, 1559.0, 655.0]], [[32.0, 419.0, 239.0, 531.0], [684.0, 443.0, 965.0, 543.0], [330.0, 418.0, 609.0, 540.0]], [[34.0, 418.0, 239.0, 529.0], [687.0, 444.0, 965.0, 542.0], [330.0, 422.0, 611.0, 539.0]], [[400.0, 482.0, 755.0, 635.0], [30.0, 419.0, 237.0, 534.0], [738.0, 619.0, 1118.0, 756.0], [748.0, 443.0, 964.0, 543.0], [325.0, 420.0, 612.0, 537.0]], [[1230.0, 446.0, 1444.0, 566.0], [27.0, 420.0, 239.0, 527.0], [685.0, 443.0, 967.0, 543.0], [327.0, 421.0, 610.0, 539.0]], [[30.0, 419.0, 237.0, 533.0], [692.0, 444.0, 965.0, 542.0], [321.0, 422.0, 609.0, 538.0]], [[29.0, 418.0, 240.0, 531.0], [685.0, 443.0, 968.0, 544.0], [325.0, 421.0, 607.0, 539.0], [694.0, 645.0, 1181.0, 756.0]], [[33.0, 419.0, 238.0, 529.0], [686.0, 444.0, 966.0, 544.0], [324.0, 420.0, 604.0, 539.0]], [[35.0, 418.0, 241.0, 531.0], [690.0, 443.0, 967.0, 542.0], [326.0, 422.0, 611.0, 539.0]], [[685.0, 444.0, 963.0, 544.0], [31.0, 420.0, 238.0, 535.0], [329.0, 423.0, 608.0, 537.0], [170.0, 505.0, 507.0, 637.0]], [[30.0, 419.0, 236.0, 535.0], [688.0, 444.0, 963.0, 543.0], [323.0, 421.0, 608.0, 540.0]], [[689.0, 444.0, 965.0, 544.0], [28.0, 418.0, 241.0, 538.0], [326.0, 421.0, 610.0, 540.0]], [[32.0, 419.0, 239.0, 536.0], [687.0, 443.0, 963.0, 543.0], [320.0, 419.0, 608.0, 539.0]], [[29.0, 419.0, 238.0, 537.0], [690.0, 444.0, 966.0, 544.0], [324.0, 418.0, 611.0, 539.0]], [[701.0, 444.0, 966.0, 542.0], [512.0, 418.0, 638.0, 540.0], [13.0, 375.0, 506.0, 662.0]]]

print "done"
print Array[:][0][0]
print Array[:][1][0]

sortedArray = np.zeros(len(Array))

print len(Array)
print len(sortedArray)

# print Array[:, 0, 0]

onlyFrameName = []
for x in range(len(Array)):
	onlyFrameName.append(Array[:][x][0])

print onlyFrameName
print "-----------"


npbbox = np.array(onlyFrameName)
sortedNpBbox = npbbox[npbbox[:, 0].argsort()]

print onlyFrameName[1][0]
print "------------"

done = []
for y in sortedNpBbox:
	for f in range(len(onlyFrameName)):
		if y[0] == onlyFrameName[f][0]:
			done.append(Array[f])

print done

print "---------"

print done[0][1:7]
print done[0][7:13]
print done[0][13:19]

total = []
for item in done:
	abc = 1
	thisItem = []
	# print "item len: ", len(item)
	while abc < len(item):
		# print "ABC: ", abc
		# print "abc + 6: ", abc+6
		# t = [abc:abc+6]
		thisItem.append(item[abc+2:abc+6])
		abc += 6
	total.append(thisItem)

print "total: ", total