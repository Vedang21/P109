import pandas as pd
import statistics 
import csv

df=pd.read_csv("studentperfoemance.csv")
writing_list=df["writing score"].to_list()
reading_list=df["reading score"].to_list()
math_list=df["math score"].to_list()
prep_list=df["test preparation course"].to_list()
launch_list=df["lunch"].to_list()
education_list=df["parental level of education"].to_list()
race_list=df["race/ethnicity"].to_list()
gender_list=df["gender"].to_list()


writing_mean=statistics.mean(writing_list)
reading_mean=statistics.mean(reading_list)
math_mean=statistics.mean(math_list)
prep_mean=statistics.mean(prep_list)
launch_mean=statistics.mean(launch_list)
education_mean=statistics.mean(education_list)
race_mean=statistics.mean(race_list)
gender_mean=statistics.mean(gender_list)

writing_median=statistics.median(writing_list)
reading_median=statistics.median(reading_list)
math_median=statistics.median(math_list)
prep_median=statistics.median(prep_list)
launch_median=statistics.median(launch_list)
education_median=statistics.median(education_list)
race_median=statistics.median(race_list)
gender_median=statistics.median(gender_list)

#height_mode=statistics.mode(height_list)
#weight_mode=statistics.mode(weight_list)

print("mean,median of height is {},{} respectively".format(height_mean,height_median))
print("mean,median of weight is {},{} respectively".format(weight_mean,weight_median))

height_sd=statistics.stdev(height_list)
height_first_sd_start,height_first_sd_end=height_mean-height_sd,height_mean+height_sd
height_second_sd_start,height_second_sd_end=height_mean-(2*height_sd),height_mean+(2*height_sd)
height_third_sd_start,height_third_sd_end=height_mean-(3*height_sd),height_mean+(3*height_sd)

weight_sd=statistics.stdev(weight_list)
weight_first_sd_start,weight_first_sd_end=weight_mean-weight_sd,weight_mean+weight_sd
weight_second_sd_start,weight_second_sd_end=weight_mean-(2*weight_sd),weight_mean+(2*weight_sd)
weight_third_sd_start,weight_third_sd_end=weight_mean-(3*weight_sd),weight_mean+(3*weight_sd)

height_list_of_data_within_1_sd=[result for result in height_list if result > height_first_sd_start and result < height_first_sd_end]
height_list_of_data_within_2_sd=[result for result in height_list if result > height_second_sd_start and result < height_second_sd_end]
height_list_of_data_within_3_sd=[result for result in height_list if result > height_third_sd_start and result < height_third_sd_end]

weight_list_of_data_within_1_sd=[result for result in weight_list if result > weight_first_sd_start and result < weight_first_sd_end]
weight_list_of_data_within_2_sd=[result for result in weight_list if result > weight_second_sd_start and result < weight_second_sd_end]
weight_list_of_data_within_3_sd=[result for result in weight_list if result > weight_third_sd_start and result < weight_third_sd_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_sd)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_sd)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_sd)*100.0/len(height_list)))

print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_sd)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_sd)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_sd)*100.0/len(weight_list)))