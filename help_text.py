help_text = dict(
    header="""This worksheet has three columns, A, B, and C that are fillable. This worksheet and instruction may use these terms
interchangeably:
- Parent A or Column A
- Parent B or Column B
- Both Parents or Column C""",
    name="""First, determine which parent is Parent A (Column A) and Parent B (Column B). If parenting time is unequal, list the
parent with more parenting time as Parent A and the other parent as Parent B.
Exception: if parents have equal parenting time, list the parent with greater monthly gross income as Parent B.""",
    line1="""**Line 1:** Enter the monthly gross income for Parent A on line 1A and Parent B on line 1B[KRS 403.212(3)(a)(b)(c) and (e)].""",
    line2="""**Line 2:** Enter the monthly amount paid by each parent for court ordered maintenance for prior spouse(s) plus the amount of
maintenance ordered in the current proceeding [KRS 403.212(3)(i)(1)] in the appropriate columns.""",
    line3="""**Line 3:** Enter the monthly amount of child support by each parent on line 3A for Parent A and line 3B for Parent B that is:
a. paid pursuant to a court/administrative order for prior-born children [KRS 403.212(3)(i)(1)];
b. paid, but not pursuant to a court/administrative order, for prior-born children for whom the parent is legally
responsible [KRS 403.212(3)(i)(2)]; and
c. imputed for prior-born children residing with the parent [KRS 403.212(3)(i)(3)].""",
    line4="""**Line 4:** Subtract any amounts on lines 2 and 3 from the amounts on line 1 for each column A and B, and enter on lines 4A and
4B. If the result is less than 0, enter 0.""",
    line5="""**Line 5:** Add the amounts on line 4 in columns A and B to obtain the combined monthly adjusted parental gross income and
enter on line 5C.""",
    line6="""**Line 6:** Divide amounts on line 4A by line 5C and 4B by line 5C. Enter Parent A’s percentage on line 6A and Parent B’s
percentage on line 6B. """,
    line7="""**Line 7:** Determine the total child support obligation by referring to the Guidelines Table [KRS 403.212(9)] using the
combined monthly adjusted gross income as entered on line 5C and the number of children for whom the parents
share a joint legal responsibility.
Before proceeding, determine whether self-support reserve (SSR) applies in the case. Check to see if Parent B’s
monthly adjusted gross income (line 4B) and the number of children for whom support is being determined falls
within the defined self-support reserve (SSR) [KRS 403.212(5)(b)].
If Parent B’s monthly adjusted gross income (line 4B) and the number of children for whom support is being
determined falls within the defined SSR, determine Parent B’s total child support obligation using only Parent B’s
monthly adjusted gross income (AGI) in the Guidelines Table and enter on line 7C [KRS 403.212(5)(b)].
If Parent B’s monthly adjusted gross income (line 4B) and the number of children for whom support is being
determined does not fall within the defined SSR, on line 7C enter the total child support obligation using the
combined monthly adjusted gross income on line 5C for the number of children for whom support is being determined
using the Child Support Guidelines Table [KRS 403.212(9)].
Check the box on line 7 (I or II) to indicate whether the total child support obligation entered on line 7C was
determined from application of the SSR using only Parent B’s monthly adjusted gross income on line 4B or the
parent’s combined monthly adjusted gross income on line 5C. Insert the amount under line 7 after checking the
appropriate box.
Only complete line 7 III if shared parenting adjustment applies. Insert the amount under line 7 after checking the
appropriate box.""",
    line8="""**Line 8:** Enter the monthly payment for childcare costs [KRS 403.211(6)] paid to the provider by Parent A on line 8A,
Parent B on line 8B, and the total of lines 8A and 8B, on line 8C. """,
    line9="""**Line 9:** Enter the monthly payment for the child(ren)’s health insurance premium or cash medical support [KRS
403.211(7)(a)] paid to the provider by Parent A on line 9A, Parent B on line 9B, and the total of lines 9A and 9B
on line 9C.""",
    line10="""**Line 10:** Add lines 7C, 8C, and 9C and enter this amount on line 10C to determine the total child support obligation with
proportionate share of the childcare and healthcare insurance cost. """,
    line11="""**Line 11:** If the total child support obligation on line 7C was not determined using the SSR, multiply line 10C by 6A and
6B to determine the monthly child support obligation of each parent. Enter Parent A’s share on line 11A and
Parent B’s share on line 11B.
If the total child support obligation on line 7C was determined using the SSR, use two methods to determine the
monthly child support obligation:
1) For Parent A, find the total child support obligation located in the Guidelines Table using the combined monthly
adjusted parental gross income on line 5C for the number of children for whom support is being determined. Enter
this amount on line 7 under 7(II). Add that amount to the total of lines 8C and 9C then multiply by 6A to
determine the monthly child support obligation of Parent A. Enter this amount on line 11A.
2) For Parent B, add lines 8C and 9C and multiply the total by 6B, and add the sum, to the SSR, on line 7C or listed
under 7(I), to calculate the monthly child support obligation of Parent B. Enter this amount on line 11B. """,
    line12="""**Line 12:** Determine the amount that each parent paid directly to the provider under lines 8 and 9. Subtract that amount from
11A for Parent A and 11B for Parent B. This new amount represents each parent’s share of their monthly child
support obligation including childcare and health insurance cost after considering any direct payments to the service
provider.
**If Shared Parenting Adjustment applies, continue to line 13 instruction. If Shared Parenting Adjustment does
not apply, skip to line 16, instruction 16, and line 16(b).**""",
    line13="""**Line 13:** Determine the number of days Parent B has the child(ren) on an annual basis based upon parenting time that is either
court-ordered or approved and consistently exercised. Enter the number under line 13B. [KRS 403.2121(2)(a)(b)]. """,
    line14="""**Line 14:** Using the days listed under line 13B, enter the adjustment percentage on line 14B using the below chart.

| **Parenting Time Days** | **Adjustment Percentage** |
|-------------------------|---------------------------|
| 73 - 87                 | 10.5%                     |
| 88 – 115                | 15%                       |
| 116 – 129               | 20.5%                     |
| 130 – 142               | 25%                       |
| 143 – 152               | 30.5%                     |
| 153 – 162               | 36%                       |
| 163 – 172               | 42%                       |
| 173 – 181               | 48.5%                     |
| 182 – 182.5             | 50%                       |
""",
    line15="""**Line 15:** Enter the parenting time credit adjustment on line 15B by multiplying the obligated parent’s adjustment percentage
(14B) by the total child support obligation (7C, SSR not applied amount).""",
    line16="""**Line 16:** This line determines the final allocated child support amount paid by Parent B:
a) **If Shared Parenting Applies:** Subtract line 15B from line 12B Parent B. If this amount is negative, Parent A
pays the positive sum of the amount in column B to Parent B.
b) **If Shared Parenting Does Not Apply:** The amount listed on line 12B is the amount Parent B is responsible for
paying as child support to Parent A. Do not proceed to line 17.""",
    line17="""**Line 17:** If Self-Support Reserve (SSR), as determined under line 7(I) is lower than the shared parenting amount listed on line
16B, Parent B pays the SSR amount determined on line 7C as their total child support obligation. If there is childcare
or health insurance cost for the minor child(ren), return to line 7, using only Parent B’s monthly adjusted gross
income and complete each step, skipping lines 13 to 15. List this amount on line 17B to show the SSR amount is
lower than the parenting time adjustment. """,
)
