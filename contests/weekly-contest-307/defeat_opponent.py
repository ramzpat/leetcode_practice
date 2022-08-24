from typing import List


class Solution:
  def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
    current_en = initialEnergy
    current_exp = initialExperience
    extra_energy = 0 
    extra_exp_need = 0
    for en, ex in zip(energy, experience):
      if current_en > en and current_exp > ex:
        current_en -= en 
        current_exp += en
      else:        
        if current_exp <= ex:
          extra_exp_need += ((ex + 1) - current_exp)
          current_exp = ex + ((ex + 1) - current_exp)
          current_exp += ex
        else:
          current_exp += ex

        if current_en <= en:
          extra_energy += ((en+1) - current_en)
          current_en = en+1
          current_en -= en

    return extra_exp_need + extra_energy