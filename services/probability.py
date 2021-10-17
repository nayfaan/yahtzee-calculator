import statistics as stat
import itertools

def score_1(roll):
    score = -1
    
    score = roll.count(1)
    
    if score < 0:
        raise ValueError('Score not calculated: '+str(roll)+'.1')
    return score

def score_2(roll):
    score = -1
    
    score = roll.count(2)*2
    
    if score < 0:
        raise ValueError('Score not calculated: '+str(roll)+'.2')
    return score

def score_3(roll):
    score = -1
    
    score = roll.count(3)*3
    
    if score < 0:
        raise ValueError('Score not calculated: '+str(roll)+'.3')
    return score

def score_4(roll):
    score = -1
    
    score = roll.count(4)*4
    
    if score < 0:
        raise ValueError('Score not calculated: '+str(roll)+'.4')
    return score

def score_5(roll):
    score = -1
    
    score = roll.count(5)*5
    
    if score < 0:
        raise ValueError('Score not calculated: '+str(roll)+'.5')
    return score

def score_6(roll):
    score = -1
    
    score = roll.count(6)*6
    
    if score < 0:
        raise ValueError('Score not calculated: '+str(roll)+'.6')
    return score

def score_ch(roll):
    score = -1
    
    score = sum(roll)
    
    if score < 0:
        raise ValueError('Score not calculated: '+str(roll)+'.ch')
    return score

def score_4k(roll):
    score = -1
    
    if len(set(roll)) <= 2 and roll.count(stat.mode(roll)) >= 4:
        score = sum(roll)
    else:
        score = 0
    
    if score < 0:
        raise ValueError('Score not calculated: '+str(roll)+'.4k')
    return score

def score_fh(roll):
    score = -1
    
    if len(set(roll)) <= 2 and (roll.count(stat.mode(roll)) == 3 or roll.count(stat.mode(roll)) == 5):
        score = sum(roll)
    else:
        score = 0
    
    if score < 0:
        raise ValueError('Score not calculated: '+str(roll)+'.fh')
    return score

def score_ss(roll):
    score = -1
    
    if set(roll).issuperset({1,2,3,4}) or set(roll).issuperset({2,3,4,5}) or set(roll).issuperset({3,4,5,6}):
        score = 15
    else:
        score = 0
    
    if score < 0:
        raise ValueError('Score not calculated: '+str(roll)+'.ss')
    return score

def score_bs(roll):
    score = -1
    
    if set(roll).issuperset({1,2,3,4,5}) or set(roll).issuperset({2,3,4,5,6}):
        score = 30
    else:
        score = 0
    
    if score < 0:
        raise ValueError('Score not calculated: '+str(roll)+'.bs')
    return score

def score_ya(roll):
    score = -1
    
    if len(set(roll)) == 1:
        score = 50
    else:
        score = 0
    
    if score < 0:
        raise ValueError('Score not calculated: '+str(roll)+'.ya')
    return score

global dice_options
dice_options = tuple(range(1,7))

def get_locked_list(roll):
    locked = []
    for dice in roll.data:
        if dice.locked:
            locked.append(dice.face)
    return sorted(locked)

def roll_results(roll):
   face_locked = get_locked_list(roll)
   possibilities = list(itertools.product(dice_options, repeat = 5 - len(face_locked)))
   
   for i in range(len(possibilities)):
       if face_locked:
           possibilities[i] = list(possibilities[i]) + face_locked
       possibilities[i] = tuple(sorted(list(possibilities[i])))
           
   possibilities = sorted(possibilities)
   return possibilities

def sort_sort_list(possibility):
    for i in range(len(possibility)):
        possibility[i] = tuple(sorted(list(possibility[i])))
    possibility = sorted(possibility)
    return possibility

#global possibilities_sorted
#possibilities_sorted = sort_sort_list(roll_results())

def set_list(possibility):
    return sorted(list(set(sort_sort_list(possibility))))

#global possibilities_set
#possibilities_set = sorted(list(set(possibilities_sorted)))

def score(face):
    return {
            "score_1": score_1(face),
            "score_2": score_2(face),
            "score_3": score_3(face),
            "score_4": score_4(face),
            "score_5": score_5(face),
            "score_6": score_6(face),
            "score_ch": score_ch(face),
            "score_4k": score_4k(face),
            "score_fh": score_fh(face),
            "score_ss": score_ss(face),
            "score_bs": score_bs(face),
            "score_ya": score_ya(face)
        }

class rolls:
    def __init__(self, data, turns_left = 2):
        if not isinstance(data, tuple):
            raise TypeError("roll must be a tuple")
        if not len(data) == 5:
            raise ValueError("Each roll must have 5 die. This roll had "+str(len(roll))+".")
        self.data = data
        self.roll = self.__roll__()
        self.face = self.__face__()
        self.lock = self.__lock__()
        self.score = score(self.face)
        self.turns_left = turns_left
    
    def __str__(self):
        s = str([str(x) for x in self.data])
        return s
    
    def __eq__(self, other):
        return (self.face, self.lock, self.turns_left) == (other.face, other.lock, other.turns_left)
    
    def __gt__(self, other):
        return (self.face, self.lock, self.turns_left) > (other.face, other.lock, other.turns_left)
    
    def __hash__(self):
        return hash((self.face, self.lock, self.turns_left))
    
    def __roll__(self):
        roll = []
        for x in self.data:
            roll.append(x.state)
        return tuple(roll)
    
    def __face__(self):
        face = []
        for x in self.roll:
            face.append(x.get("face"))
        return tuple(face)
    
    def __lock__(self):
        lock = []
        for x in self.roll:
            lock.append(x.get("locked"))
        return tuple(lock)
    
class dice:
    def __init__(self, face, locked = False):
        if not isinstance(face, int):
            raise TypeError("face must be an int")
        if face > 6 or face < 1:
            raise ValueError("face ("+str(face)+") must be between 1-6")
        if not isinstance(locked, bool):
            raise TypeError("locked must be a bool")
        self.face = face
        self.locked = locked
        self.state = {"face": face, "locked": locked}
        
    def __str__(self):
        return str(self.state)
    
    def __eq__(self, other):
        return (self.face, self.locked) == (other.face, other.locked)
    
    def __gt__(self, other):
        return (self.face, self.locked) > (other.face, other.locked)
    
    def __hash__(self):
        return hash((self.face, self.locked))

def face2data(face):
    data = list(face)
    
    for i in range(len(data)):
        data[i] = dice(data[i],False)
    
    return tuple(data)

global expect_base_dict
expect_base_dict = {
        "score_1": 0,
        "score_2": 0,
        "score_3": 0,
        "score_4": 0,
        "score_5": 0,
        "score_6": 0,
        "score_ch": 0,
        "score_4k": 0,
        "score_fh": 0,
        "score_ss": 0,
        "score_bs": 0,
        "score_ya": 0
    }

def calc_probability(face, roll):
    conditional_base = roll_results(roll)
    prob = conditional_base.count(tuple(sorted(list(face))))/len(conditional_base)
    return prob

def expected(roll):
    expected_score = expect_base_dict
    for face in set_list(roll_results(roll)):
        score_list = rolls(face2data(face)).score
        for score_item in expected_score.keys():
            expected_score[score_item] += score_list[score_item] * calc_probability(face,roll)
    return expected_score

def sublist(parent_list,child_list):
    sublist = True
    
    for y in set(child_list):
        if parent_list.count(y) < child_list.count(y):
            sublist = False
            
    return sublist

'''def roll_possibilities_locked(roll):
    face_locked = get_locked_list(roll)
            
    if len(face_locked) >= 5:
        possibilities_locked = [tuple(sorted(face_locked))]
    else:
        possibilities_locked = roll_results(face_locked)
    
    #possibilities.append(tuple([i1+1,i2+1,i3+1,i4+1,i5+1]))
    
    return possibilities_locked'''

def roll_results_probability(roll):
    probability_dict = {}
    for face in set_list(roll_results(roll)):
        probability_dict.update({face:{"probability": calc_probability(face,roll), "score": score(face)}})
    return probability_dict

def decision_tree(roll):
    lock_decision_tree_temp = set()
    lock_decision_tree = []
    lock_matrix = list(itertools.product((False, True), repeat = 5))
    for lock_route in lock_matrix:
        for i in range(len(lock_route)):
            roll_data = (
                dice(roll.face[0],lock_route[0]),
                dice(roll.face[1],lock_route[1]),
                dice(roll.face[2],lock_route[2]),
                dice(roll.face[3],lock_route[3]),
                dice(roll.face[4],lock_route[4])
                )
            
            temp_size = len(lock_decision_tree_temp)
            lock_decision_tree_temp.add(tuple(sorted(roll_data)))
            if not len(lock_decision_tree_temp) == temp_size:
                lock_decision_tree.append(rolls(roll_data, roll.turns_left - 1))
            
    return tuple(lock_decision_tree)

def full_analysis(roll):
    #WIP Reursion
    
    
    
    full_roll_tree = {}
    
    roll_tree = {}
    
    for x in decision_tree(roll):
        '''x_results = roll_results(x)
        x_results_with_probability_score = {}
        for y in x_results:
            x_results_with_probability_score.update({y: roll_results_probability(y)})'''
        roll_tree.update({x: roll_results_probability(x) })
        
    full_roll_tree.update({roll: roll_tree})
    
    roll.turns_left -= 1
    
    return full_roll_tree

if __name__ == "__main__":
    dice1 = dice(1,False)
    dice2 = dice(4,False)
    dice3 = dice(2,False)
    dice4 = dice(2,False)
    dice5 = dice(3,False)
    roll = rolls((dice1,dice2,dice3,dice4,dice5))

    print(full_analysis(roll))