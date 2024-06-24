YEAR_DAYS = 365
MIN_SPA_DAYS = 73
TIME_ADJUSTMENT = """73 10.5
88 15
116 20.5
130 25
143 30.5
153 36
163 42
173 48.5
182 50"""

SSR_TABLE = """0 60 60 60 60 60 60
100 60 60 60 60 60 60
200 60 60 60 60 60 60
300 60 60 60 60 60 60
400 60 60 60 60 60 60
500 60 60 60 60 60 60
600 60 60 60 60 60 60
700 60 60 60 60 60 60
800 60 60 60 60 60 60
900 60 60 60 60 60 60
1000 85 85 85 85 85 85
1100 148 150 152 154 155 157
1200 200 231 234 237 239 242
1300 216 312 316 320 323 327
1400 231 339 398 403 407 412
1500 247 362 437 486 491 497
1600 262 384 464 518 570 582"""

# GUIDELINES
# KRS 403.212(9)
# https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=52811
GUIDELINES = """0 60 60 60 60 60 60
100 60 60 60 60 60 60
200 60 60 60 60 60 60
300 60 60 60 60 60 60
400 60 60 60 60 60 60
500 60 60 60 60 60 60
600 60 60 60 60 60 60
700 60 60 60 60 60 60
800 60 60 60 60 60 60
900 60 60 60 60 60 60
1,000 85 85 85 85 85 85
1,100 148 150 152 154 155 157
1,200 200 231 234 237 239 242
1,300 216 312 316 320 323 327
1,400 231 339 398 403 407 412
1,500 247 362 437 486 491 497
1,600 262 384 464 518 570 582
1,700 277 406 491 548 603 655
1,800 292 428 517 578 635 691
1,900 307 450 544 607 668 726
2,000 322 472 570 637 701 762
2,100 337 494 597 667 734 797
2,200 352 516 624 697 766 833
2,300 367 538 650 726 799 869
2,400 382 560 677 756 832 904
2,500 397 582 704 786 865 940
2,600 412 604 730 816 897 975
2,700 427 626 757 845 930 1,011
2,800 442 648 783 875 963 1,046
2,900 457 670 810 905 995 1,082
3,000 472 692 837 935 1,028 1,118
3,100 487 714 863 964 1,061 1,153
3,200 502 737 890 994 1,094 1,189
3,300 517 759 917 1,024 1,126 1,224
3,400 532 781 943 1,054 1,159 1,260
3,500 547 803 970 1,083 1,192 1,295
3,600 562 825 997 1,113 1,224 1,331
3,700 577 847 1,023 1,143 1,257 1,367
3,800 592 869 1,050 1,173 1,290 1,402
3,900 607 891 1,076 1,202 1,323 1,438
4,000 621 912 1,102 1,230 1,353 1,471
4,100 634 931 1,125 1,256 1,382 1,502
4,200 647 950 1,148 1,282 1,410 1,533
4,300 660 969 1,171 1,308 1,439 1,564
4,400 673 988 1,194 1,334 1,467 1,595
4,500 686 1,007 1,217 1,359 1,495 1,625
4,600 699 1,026 1,240 1,385 1,524 1,656
4,700 712 1,045 1,263 1,411 1,552 1,687
4,800 725 1,064 1,286 1,437 1,580 1,718
4,900 738 1,084 1,309 1,463 1,609 1,749
5,000 751 1,103 1,332 1,488 1,637 1,780
5,100 764 1,122 1,356 1,514 1,666 1,810
5,200 777 1,141 1,379 1,540 1,694 1,841
5,300 790 1,160 1,402 1,566 1,722 1,872
5,400 799 1,172 1,415 1,581 1,739 1,890
5,500 805 1,177 1,419 1,585 1,744 1,896
5,600 810 1,181 1,423 1,590 1,749 1,901
5,700 815 1,186 1,427 1,594 1,753 1,906
5,800 820 1,191 1,431 1,598 1,758 1,911
5,900 825 1,195 1,435 1,603 1,763 1,916
6,000 831 1,200 1,439 1,607 1,768 1,922
6,100 837 1,208 1,449 1,618 1,780 1,935
6,200 844 1,217 1,459 1,629 1,792 1,948
6,300 851 1,226 1,469 1,641 1,805 1,962
6,400 858 1,234 1,479 1,652 1,817 1,975
6,500 865 1,243 1,489 1,663 1,829 1,988
6,600 871 1,251 1,499 1,674 1,841 2,002
6,700 881 1,263 1,513 1,690 1,859 2,021
6,800 892 1,278 1,530 1,709 1,880 2,044
6,900 903 1,292 1,548 1,729 1,902 2,067
7,000 914 1,306 1,565 1,748 1,923 2,090
7,100 925 1,320 1,582 1,767 1,944 2,113
7,200 935 1,335 1,600 1,787 1,965 2,136
7,300 946 1,348 1,616 1,805 1,986 2,159
7,400 954 1,360 1,630 1,820 2,003 2,177
7,500 962 1,372 1,643 1,836 2,019 2,195
7,600 969 1,384 1,657 1,851 2,036 2,213
7,700 977 1,396 1,670 1,866 2,052 2,231
7,800 984 1,407 1,683 1,880 2,068 2,248
7,900 991 1,419 1,696 1,895 2,084 2,266
8,000 996 1,426 1,704 1,903 2,094 2,276
8,100 1,000 1,429 1,709 1,908 2,099 2,282
8,200 1,004 1,433 1,713 1,914 2,105 2,288
8,300 1,008 1,437 1,718 1,919 2,110 2,294
8,400 1,012 1,441 1,722 1,924 2,116 2,300
8,500 1,016 1,444 1,727 1,929 2,122 2,306
8,600 1,020 1,448 1,731 1,934 2,127 2,312
8,700 1,026 1,456 1,740 1,944 2,138 2,324
8,800 1,033 1,464 1,749 1,953 2,149 2,336
8,900 1,039 1,472 1,758 1,963 2,160 2,347
9,000 1,046 1,480 1,766 1,973 2,170 2,359
9,100 1,052 1,488 1,775 1,983 2,181 2,371
9,200 1,059 1,496 1,784 1,993 2,192 2,382
9,300 1,065 1,502 1,792 2,002 2,202 2,393
9,400 1,070 1,507 1,799 2,010 2,211 2,403
9,500 1,075 1,511 1,807 2,018 2,220 2,413
9,600 1,080 1,516 1,814 2,026 2,229 2,423
9,700 1,085 1,520 1,822 2,035 2,238 2,433
9,800 1,090 1,524 1,829 2,043 2,247 2,443
9,900 1,094 1,529 1,836 2,051 2,256 2,453
10,000 1,099 1,533 1,844 2,059 2,265 2,463
10,100 1,104 1,538 1,851 2,068 2,275 2,472
10,200 1,109 1,542 1,859 2,076 2,284 2,482
10,300 1,115 1,549 1,867 2,086 2,294 2,494
10,400 1,123 1,560 1,878 2,098 2,308 2,509
10,500 1,130 1,571 1,889 2,110 2,321 2,523
10,600 1,137 1,582 1,900 2,123 2,335 2,538
10,700 1,145 1,593 1,911 2,135 2,349 2,553
10,800 1,152 1,604 1,922 2,147 2,362 2,568
10,900 1,159 1,615 1,933 2,160 2,376 2,582
11,000 1,167 1,626 1,944 2,172 2,389 2,597
11,100 1,174 1,637 1,956 2,185 2,403 2,612
11,200 1,182 1,649 1,968 2,198 2,418 2,628
11,300 1,191 1,661 1,980 2,212 2,433 2,644
11,400 1,199 1,673 1,992 2,225 2,448 2,660
11,500 1,207 1,685 2,004 2,239 2,462 2,677
11,600 1,215 1,695 2,016 2,252 2,477 2,693
11,700 1,222 1,705 2,029 2,266 2,493 2,710
11,800 1,229 1,714 2,041 2,280 2,508 2,726
11,900 1,237 1,723 2,054 2,294 2,523 2,743
12,000 1,244 1,732 2,066 2,308 2,539 2,759
12,100 1,252 1,742 2,078 2,322 2,554 2,776
12,200 1,259 1,751 2,091 2,336 2,569 2,793
12,300 1,267 1,760 2,103 2,349 2,584 2,809
12,400 1,274 1,769 2,116 2,363 2,600 2,826
12,500 1,282 1,778 2,128 2,377 2,615 2,842
12,600 1,289 1,788 2,141 2,391 2,630 2,859
12,700 1,296 1,797 2,153 2,405 2,645 2,876
12,800 1,304 1,806 2,165 2,419 2,661 2,892
12,900 1,311 1,815 2,178 2,433 2,676 2,909
13,000 1,319 1,825 2,190 2,447 2,691 2,925
13,100 1,326 1,834 2,203 2,461 2,707 2,942
13,200 1,334 1,843 2,215 2,474 2,722 2,959
13,300 1,341 1,852 2,228 2,488 2,737 2,975
13,400 1,348 1,861 2,238 2,500 2,750 2,990
13,500 1,353 1,868 2,247 2,510 2,761 3,001
13,600 1,359 1,875 2,255 2,519 2,771 3,012
13,700 1,364 1,882 2,264 2,529 2,781 3,023
13,800 1,370 1,889 2,272 2,538 2,792 3,035
13,900 1,375 1,896 2,281 2,547 2,802 3,046
14,000 1,381 1,903 2,289 2,557 2,812 3,057
14,100 1,386 1,910 2,297 2,566 2,822 3,068
14,200 1,391 1,916 2,304 2,574 2,831 3,078
14,300 1,396 1,922 2,312 2,582 2,841 3,088
14,400 1,401 1,929 2,319 2,591 2,850 3,098
14,500 1,406 1,935 2,327 2,599 2,859 3,108
14,600 1,410 1,941 2,334 2,607 2,868 3,118
14,700 1,415 1,947 2,342 2,616 2,877 3,128
14,800 1,420 1,954 2,349 2,624 2,886 3,138
14,900 1,425 1,960 2,357 2,632 2,896 3,147
15,000 1,430 1,966 2,364 2,641 2,905 3,157
15,100 1,435 1,972 2,371 2,649 2,914 3,167
15,200 1,440 1,978 2,379 2,657 2,923 3,177
15,300 1,444 1,985 2,386 2,666 2,932 3,187
15,400 1,449 1,991 2,394 2,674 2,941 3,197
15,500 1,454 1,997 2,401 2,682 2,950 3,207
15,600 1,459 2,003 2,409 2,691 2,960 3,217
15,700 1,464 2,010 2,416 2,699 2,969 3,227
15,800 1,469 2,016 2,424 2,707 2,978 3,237
15,900 1,474 2,022 2,431 2,715 2,987 3,247
16,000 1,478 2,028 2,439 2,724 2,996 3,257
16,100 1,484 2,035 2,445 2,732 3,005 3,266
16,200 1,490 2,041 2,452 2,739 3,013 3,275
16,300 1,495 2,047 2,459 2,747 3,022 3,285
16,400 1,501 2,053 2,466 2,755 3,030 3,294
16,500 1,506 2,059 2,473 2,763 3,039 3,303
16,600 1,512 2,065 2,480 2,770 3,047 3,313
16,700 1,518 2,071 2,487 2,778 3,056 3,322
16,800 1,523 2,077 2,494 2,786 3,065 3,331
16,900 1,529 2,083 2,501 2,794 3,073 3,340
17,000 1,534 2,089 2,508 2,801 3,082 3,350
17,100 1,540 2,095 2,515 2,809 3,090 3,359
17,200 1,545 2,102 2,522 2,817 3,099 3,368
17,300 1,551 2,108 2,529 2,825 3,107 3,378
17,400 1,557 2,114 2,536 2,832 3,116 3,387
17,500 1,562 2,120 2,543 2,840 3,124 3,396
17,600 1,568 2,126 2,550 2,848 3,133 3,405
17,700 1,573 2,132 2,557 2,856 3,141 3,415
17,800 1,579 2,138 2,563 2,863 3,149 3,423
17,900 1,584 2,144 2,570 2,870 3,157 3,432
18,000 1,589 2,149 2,576 2,878 3,166 3,441
18,100 1,595 2,155 2,583 2,885 3,174 3,450
18,200 1,600 2,161 2,590 2,893 3,182 3,459
18,300 1,605 2,167 2,596 2,900 3,190 3,467
18,400 1,611 2,173 2,603 2,907 3,198 3,476
18,500 1,616 2,178 2,609 2,915 3,206 3,485
18,600 1,621 2,184 2,616 2,922 3,214 3,494
18,700 1,627 2,190 2,623 2,929 3,222 3,503
18,800 1,632 2,196 2,629 2,937 3,231 3,512
18,900 1,637 2,202 2,636 2,944 3,239 3,520
19,000 1,642 2,207 2,642 2,952 3,247 3,529
19,100 1,648 2,213 2,649 2,959 3,255 3,538
19,200 1,653 2,219 2,656 2,966 3,263 3,547
19,300 1,658 2,225 2,662 2,974 3,271 3,556
19,400 1,664 2,231 2,669 2,981 3,279 3,565
19,500 1,669 2,236 2,675 2,989 3,287 3,573
19,600 1,674 2,242 2,682 2,996 3,295 3,582
19,700 1,680 2,248 2,689 3,003 3,304 3,591
19,800 1,685 2,254 2,695 3,011 3,312 3,600
19,900 1,690 2,260 2,702 3,018 3,320 3,609
20,000 1,696 2,265 2,709 3,025 3,328 3,617
20,100 1,701 2,271 2,715 3,033 3,336 3,626
20,200 1,706 2,277 2,722 3,040 3,344 3,635
20,300 1,710 2,282 2,728 3,047 3,352 3,643
20,400 1,713 2,287 2,733 3,053 3,358 3,651
20,500 1,717 2,292 2,739 3,059 3,365 3,658
20,600 1,720 2,297 2,745 3,066 3,372 3,666
20,700 1,723 2,302 2,750 3,072 3,379 3,673
20,800 1,726 2,307 2,756 3,078 3,386 3,681
20,900 1,730 2,313 2,761 3,084 3,393 3,688
21,000 1,733 2,318 2,767 3,091 3,400 3,695
21,100 1,736 2,323 2,773 3,097 3,407 3,703
21,200 1,739 2,328 2,778 3,103 3,413 3,710
21,300 1,743 2,333 2,784 3,109 3,420 3,718
21,400 1,746 2,338 2,789 3,116 3,427 3,725
21,500 1,749 2,343 2,795 3,122 3,434 3,733
21,600 1,752 2,348 2,801 3,128 3,441 3,740
21,700 1,756 2,353 2,806 3,134 3,448 3,748
21,800 1,759 2,358 2,812 3,141 3,455 3,755
21,900 1,762 2,363 2,817 3,147 3,462 3,763
22,000 1,765 2,368 2,823 3,153 3,469 3,770
22,100 1,769 2,373 2,829 3,160 3,475 3,778
22,200 1,772 2,378 2,834 3,166 3,482 3,785
22,300 1,775 2,383 2,840 3,172 3,489 3,793
22,400 1,778 2,388 2,845 3,178 3,496 3,800
22,500 1,782 2,393 2,851 3,185 3,503 3,808
22,600 1,785 2,398 2,857 3,191 3,510 3,815
22,700 1,788 2,403 2,862 3,197 3,517 3,823
22,800 1,791 2,408 2,868 3,203 3,524 3,830
22,900 1,795 2,413 2,873 3,210 3,531 3,838
23,000 1,798 2,418 2,879 3,216 3,537 3,845
23,100 1,801 2,423 2,885 3,222 3,544 3,853
23,200 1,804 2,429 2,890 3,228 3,551 3,860
23,300 1,808 2,434 2,896 3,235 3,558 3,868
23,400 1,811 2,439 2,901 3,241 3,565 3,875
23,500 1,814 2,444 2,907 3,247 3,572 3,883
23,600 1,817 2,449 2,913 3,253 3,579 3,890
23,700 1,821 2,454 2,918 3,260 3,586 3,898
23,800 1,824 2,459 2,924 3,266 3,593 3,905
23,900 1,827 2,464 2,929 3,272 3,599 3,913
24,000 1,830 2,469 2,935 3,278 3,606 3,920
24,100 1,834 2,474 2,941 3,285 3,613 3,928
24,200 1,837 2,479 2,946 3,291 3,620 3,935
24,300 1,840 2,484 2,952 3,297 3,627 3,943
24,400 1,843 2,489 2,957 3,304 3,634 3,950
24,500 1,847 2,494 2,963 3,310 3,641 3,957
24,600 1,850 2,499 2,969 3,316 3,648 3,965
24,700 1,853 2,504 2,974 3,322 3,655 3,972
24,800 1,856 2,509 2,980 3,329 3,661 3,980
24,900 1,860 2,514 2,986 3,335 3,668 3,987
25,000 1,863 2,519 2,991 3,341 3,675 3,995
25,100 1,866 2,524 2,997 3,347 3,682 4,002
25,200 1,869 2,529 3,002 3,354 3,689 4,010
25,300 1,873 2,534 3,008 3,360 3,696 4,017
25,400 1,876 2,540 3,014 3,366 3,703 4,025
25,500 1,879 2,545 3,019 3,372 3,710 4,032
25,600 1,882 2,550 3,025 3,379 3,716 4,040
25,700 1,886 2,555 3,030 3,385 3,723 4,047
25,800 1,889 2,560 3,036 3,391 3,730 4,055
25,900 1,892 2,565 3,042 3,397 3,737 4,062
26,000 1,895 2,570 3,047 3,404 3,744 4,070"""
