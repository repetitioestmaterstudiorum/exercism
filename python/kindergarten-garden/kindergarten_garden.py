class Garden:
    def __init__(self, diagram, students = None):
        self.students = sorted(students) if students else ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

        self.plant_rows = diagram.splitlines()

        self.plant_dict = {'V': 'Violets', 'R': 'Radishes', 'C': 'Clover', 'G': 'Grass'}

    def plants(self, plant_owner):
        plant_spot_start = self.students.index(plant_owner) * 2

        plant_one = self.plant_rows[0][plant_spot_start]
        plant_two = self.plant_rows[0][plant_spot_start + 1]
        plant_three = self.plant_rows[1][plant_spot_start]
        plant_four = self.plant_rows[1][plant_spot_start + 1]

        return [self.plant_dict[plant_one], self.plant_dict[plant_two], self.plant_dict[plant_three], self.plant_dict[plant_four]]

# --- alternative solution
# class Garden:
#     def __init__(self, diagram, students = None):
#         self.students = sorted(students) if students else ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

#         d = diagram.replace('\n', '')
#         d_half_len = int(len(diagram) / 2)
#         self.plant_sets = [d[x] + d[x + 1] + d[x + d_half_len] + d[x + d_half_len + 1] for x in range(d_half_len) if x % 2 == 0]

#     def plants(self, plant_owner):
#         return [{'V': 'Violets', 'R': 'Radishes', 'C': 'Clover', 'G': 'Grass'}[x] for x in self.plant_sets[self.students.index(plant_owner)]]

# --- quick tests
garden = Garden("RC\nGG")
print(garden.plants('Alice')) # ["Radishes", "Clover", "Grass", "Grass"]
#
garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
print(garden.plants("Larry")) # ['Grass', 'Violets', 'Clover', 'Violets']
