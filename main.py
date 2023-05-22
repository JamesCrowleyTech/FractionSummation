from data.hard_values import *
from fractions import Fraction
from copy import copy
from random import random


nums = [3,4,6,8,12,24]

best_nums = []
loops = 1000
for z in range(loops):
    destruction_loops = 1

    if len(nums) > len(best_nums):
        best_nums = copy(nums)

    print(len(nums), len(list(set(nums))), z, len(best_nums),)

    for _ in range(2):
        to_add = []
        to_delete = []
        for i in range(len(nums)):
            num = nums[i]
            if num not in all_2_factors:
                continue
            should_break = False
            for factors in all_2_factors[num]:
                in_nums = []
                for factor in factors:
                    if factor in nums:
                        in_nums.append(factor)
                if len(in_nums) == 2: continue
                elif len(in_nums) == 0:
                    to_add.append(factors[0])
                    to_add.append(factors[1])
                    to_delete.append(num)
                    break
                elif len(in_nums) == 1: continue
                elif len(in_nums) == 1 and in_nums[0] in recompositions:
                    for recomp in recompositions[in_nums[0]]:
                        if recomp not in nums or recomp in factors or recomp == in_nums[0] or recomp == num: continue
                        nf = Fraction(1, recomp) + Fraction(1, in_nums[0])
                        if nf.denominator in nums: continue
                        f_add = [a for a in factors if (a != in_nums[0])][0]
                        if f_add == nf.denominator: continue
                        to_add.extend([f_add, nf.denominator])
                        to_delete.extend([num, in_nums[0], recomp])
                        should_break = True
                        break
                    if should_break: break
            for n in to_delete:

                nums.remove(n)
            nums += to_add
            to_delete.clear()
            to_add.clear()

    for i in range(1):

        to_add = []
        to_delete = []
        should_break = False
        for j in range(len(nums) - 1, -1, -1):
            num = nums[j]
            if num > 670: continue
            if num not in all_3_factors:
                continue

            potentials = []
            for factors in all_3_factors[num]:
                factors_in_nums = []

                for factor in factors:
                    if factor in nums:
                        factors_in_nums.append(factor)
                should_break = False
                potentials = []
                if len(factors_in_nums) == 0:
                    to_add.extend(factors)
                    to_delete.append(num)
                    should_break = True
                    break
                if len(factors_in_nums) == 1:
                    to_recompose = factors_in_nums[0]
                    pf = Fraction(1, to_recompose)
                    if to_recompose not in recompositions: continue
                    for p in recompositions[to_recompose]:
                        nf = Fraction(Fraction(1, p) + pf).denominator
                        if nf in nums or nf in factors: continue
                        if p in nums and p not in factors and p != num:

                            to_delete.extend([p, to_recompose, num])
                            to_add.extend(factors)
                            to_add.append(nf)
                            should_break = True
                            break
                    if should_break: break


                if len(factors_in_nums) != 2: continue
                to_recompose1 = factors_in_nums[0]
                to_recompose2 = factors_in_nums[1]
                pf1 = Fraction(1, to_recompose1)
                pf2 = Fraction(1, to_recompose2)
                if to_recompose1 not in recompositions or to_recompose2 not in recompositions:
                    continue
                partner1 = partner2 = None
                for p in recompositions[to_recompose1]:
                    d = Fraction(pf1 + Fraction(1, p)).denominator
                    if p in nums and p not in factors and d not in nums and d not in factors and p != num:
                        partner1 = p
                for p in recompositions[to_recompose2]:
                    d = Fraction(pf2 + Fraction(1, p)).denominator
                    if p in nums and p not in factors and p != partner1 and d not in nums and d not in factors and p != num:
                        partner2 = p
                if partner1 and partner2:
                    if Fraction(Fraction(1, partner1) + pf1).denominator == Fraction(Fraction(1, partner2) + pf2).denominator: continue
                    to_delete.extend([partner1, partner2, to_recompose1, to_recompose2, num])
                    to_add.extend(factors)
                    to_add.extend([Fraction(Fraction(1, partner1) + pf1).denominator, Fraction(Fraction(1, partner2) + pf2).denominator])
                    should_break = True
                    break
            if should_break:
                break

        if to_delete:
            for n in to_delete:
                nums.remove(n)
            nums += to_add
            to_delete.clear()
            to_add.clear()



    for _ in range(1):
        if z < 40: continue
        to_add = []
        to_delete = []
        should_break = False
        for i, num in enumerate(nums):
            if num > 495: continue
            if num not in all_4_factors:
                continue

            for factors in all_4_factors[num]:
                factors_in_nums = []

                for factor in factors:
                    if factor in nums:
                        factors_in_nums.append(factor)


                if not factors_in_nums:
                    to_add.extend(factors)
                    to_delete.append(num)
                    break
                elif len(factors_in_nums) == 1:
                    to_recompose = factors_in_nums[0]
                    pf = Fraction(1, to_recompose)
                    if to_recompose not in recompositions: continue
                    for p in recompositions[to_recompose]:
                        nf = Fraction(Fraction(1, p) + pf).denominator
                        if nf in nums or nf in factors: continue
                        if p in nums and p not in factors and p != num:

                            to_delete.extend([p, to_recompose, num])
                            to_add.extend(factors)
                            to_add.append(nf)
                            should_break = True
                            break

                elif len(factors_in_nums) == 2:

                    to_recompose1 = factors_in_nums[0]
                    to_recompose2 = factors_in_nums[1]
                    pf1 = Fraction(1, to_recompose1)
                    pf2 = Fraction(1, to_recompose2)
                    if to_recompose1 not in recompositions or to_recompose2 not in recompositions:
                        continue
                    partner1 = partner2 = None
                    for p in recompositions[to_recompose1]:
                        d = Fraction(pf1 + Fraction(1, p)).denominator
                        if p in nums and p not in factors and d not in nums and d not in factors and p != num:
                            partner1 = p
                    for p in recompositions[to_recompose2]:
                        d = Fraction(pf2 + Fraction(1, p)).denominator
                        if p in nums and p not in factors and p != partner1 and d not in nums and d not in factors and p != num:
                            partner2 = p
                    if partner1 and partner2:
                        if Fraction(Fraction(1, partner1) + pf1).denominator == Fraction(Fraction(1, partner2) + pf2).denominator: continue
                        to_delete.extend([partner1, partner2, to_recompose1, to_recompose2, num])
                        to_add.extend(factors)
                        to_add.extend([Fraction(Fraction(1, partner1) + pf1).denominator, Fraction(Fraction(1, partner2) + pf2).denominator])
                        should_break = True
                        break
                if should_break: break
                elif len(factors_in_nums) == 3:
                    to_recompose1 = factors_in_nums[0]
                    to_recompose2 = factors_in_nums[1]
                    to_recompose3 = factors_in_nums[2]
                    pf1 = Fraction(1, to_recompose1)
                    pf2 = Fraction(1, to_recompose2)
                    pf3 = Fraction(1, to_recompose3)
                    if to_recompose1 not in recompositions or to_recompose2 not in recompositions or to_recompose3 not in recompositions:
                        continue
                    partner1 = partner2 = partner3 = None
                    for p in recompositions[to_recompose1]:
                        d = Fraction(pf1 + Fraction(1, p)).denominator
                        if p in nums and p not in factors and d not in nums and d not in factors and p != num:
                            partner1 = p
                    if not partner1: continue
                    for p in recompositions[to_recompose2]:
                        d = Fraction(pf2 + Fraction(1, p)).denominator
                        if p in nums and p not in factors and p != partner1 and d not in nums and d not in factors and p != num:
                            partner2 = p
                    if not partner2: continue
                    for p in recompositions[to_recompose3]:
                        d = Fraction(pf3 + Fraction(1, p)).denominator
                        if p in nums and p not in factors and p != partner1 and p!= partner2 and d not in nums and d not in factors and p != num:
                            partner3 = p
                    if not partner3: continue
                    nf1 = Fraction(Fraction(1, partner1) + pf1).denominator
                    nf2 = Fraction(Fraction(1, partner2) + pf2).denominator
                    nf3 = Fraction(Fraction(1, partner3) + pf3).denominator
                    if len({nf1, nf2, nf3}) <= 2: continue
                    to_delete.extend([partner1, partner2, partner3, to_recompose1, to_recompose2, to_recompose3, num])
                    to_add.extend(factors)
                    to_add.extend([nf1, nf2, nf3])
                    should_break = True
                    break
            for n in to_delete:
                nums.remove(n)
            nums += to_add
            to_delete.clear()
            to_add.clear()
            if should_break: break

    for _ in range(1):
        for num in nums:
            setnums = set(nums)
            if num not in equivalencies_2_factors: continue
            to_delete = []
            to_add = []
            for factors in equivalencies_2_factors[num]:
                f1 = factors[0]
                f2 = factors[1]
                f3 = factors[2]
                if f1 not in setnums or f2 in setnums or f3 in setnums: continue
                to_delete.extend([num, f1])
                to_add.extend([f2, f3])
                break
            if not to_delete: continue

            for f in to_delete: nums.remove(f)
            for f in to_add: nums.append(f)
            break

best_nums.sort()
print(str(best_nums).replace(" ", ""))
print("\n" + str(len(best_nums)) + "\n")
out = [1 / x for x in best_nums]
print(sum(out))
print(len(list(set(best_nums))))

# for _ in range(destruction_loops):
    #     if random() > 1:
    #         continue
    #     should_break = False
    #     for i in range(len(nums)):
    #         # if random() < 0.5:
    #         #     break
    #         # print(i, len(nums) - 1, nums[i], )
    #         num = nums[i]
    #
    #         if num == 2:
    #             continue
    #         if num not in recompositions_3_factors: continue
    #         for factors in recompositions_3_factors[num]:
    #             new_fraction = str(
    #                 Fraction(Fraction(1, num) + Fraction(1, factors[0]) + Fraction(1, factors[1]))).split("/")
    #             new_numerator = int(new_fraction[0])
    #             new_denominator = int(new_fraction[1])
    #             if not (factors[0] in nums and factors[1] in nums):
    #                 continue
    #             if new_numerator != 1:
    #                 continue
    #             if new_denominator in nums:
    #                 continue
    #             nums.remove(num)
    #             nums.remove(factors[0])
    #             nums.remove(factors[1])
    #             nums.append(new_denominator)
    #             should_break = True
    #             break
    #         if should_break:
    #             break
    #     pass

    # for _ in range(destruction_loops):
    #     if random() > 1:
    #         continue
    #     r = randint(0, len(nums) - 1)
    #     for i in range(r, len(nums)):
    #         num = nums[i]
    #         if num == 2:
    #             continue
    #         if num not in recompositions:
    #             continue
    #         should_break = False
    #         for v in recompositions[num]:
    #             total_fraction = Fraction(Fraction(1, num) + Fraction(1, v))
    #             new_denominator = int(str(total_fraction).split("/")[1])
    #             # pr
    #             if v in nums and new_denominator not in nums:
    #                 # print(num, v, new_denominator)
    #                 nums.append(new_denominator)
    #                 nums.remove(num)
    #                 nums.remove(v)
    #                 should_break = True
    #                 break
    #         if should_break:
    #             break

    # for _ in range(destruction_loops):
    #     if not random() > 0.3:
    #         continue
    #     should_break = False
    #     for i in range(len(nums)):
    #         # if random() < 0.5:
    #         #     break
    #         # print(i, len(nums) - 1, nums[i], )
    #         num = nums[i]
    #
    #         if num == 2:
    #             continue
    #         if num not in recompositions_4_factors: continue
    #         for factors in recompositions_4_factors[num]:
    #             new_fraction = str(
    #                 Fraction(Fraction(1, num) + Fraction(1, factors[0]) + Fraction(1, factors[1]) + Fraction(1, factors[2]))).split("/")
    #             new_numerator = int(new_fraction[0])
    #             new_denominator = int(new_fraction[1])
    #             if not (factors[0] in nums and factors[1] in nums and factors[2] in nums):
    #                 continue
    #             if new_numerator != 1:
    #                 continue
    #             if new_denominator in nums:
    #                 continue
    #             nums.remove(num)
    #             nums.remove(factors[0])
    #             nums.remove(factors[1])
    #             nums.remove(factors[2])
    #             nums.append(new_denominator)
    #             should_break = True
    #             break
    #         if should_break:
    #             break