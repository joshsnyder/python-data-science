# The purpose of this program is to demistrate the copy function utilizing it for shallow and deep copies of another object.
# Joshua Snyder 03/08/2020

# External modules
import copy

# Global data set
trailBlazers = [{"Microsoft":{"Bill Gates"},"Apple":{"Steve Jobs"},"Amazon":{"Jeff Bezos"}}]

def main():
    # Shallow copy
    ShallowCopy()
    # Deep copy
    DeepCopy()

def ShallowCopy():
    print("-------------------------------------------------------")
    print("--------------- Shallow Copy Example ------------------")
    print("-------------------------------------------------------")
    print(f"Original data set before shallow copy: {trailBlazers}")
    shallow = copy.copy(trailBlazers)
    print(f"Shallow copy: {shallow}")
    shallow[0]['Apple'] = "{Steve Wozniak}"
    print(f"Shallow copy after update: {shallow}")
    print(f"Original data set after shallow copy: {trailBlazers}")

def DeepCopy():
    print("-------------------------------------------------------")
    print("---------------- Deep Copy Example --------------------")
    print("-------------------------------------------------------")
    print(f"Original data set before deep copy: {trailBlazers}")
    deep = copy.deepcopy(trailBlazers)
    print(f"Deep copy: {deep}")
    deep[0]['Apple'] = '{Steve Jobs}'
    print(f"Deep copy after update: {deep}")
    print(f"Original data set after deep copy: {trailBlazers}")

# Execute program
main()