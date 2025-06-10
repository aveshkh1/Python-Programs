#Dictionary is built-in data type that is used to store data in key value pairs
#dicionary is unordered collection of items and they don't allow duplicate keys
dict={
    "student_names":["Avesh","Tanu","Aishu","Ammu","Gundu"],
    "marks":{
        "Puc":[75,78,77,67,55,23],
        "SSLC":[80,75,67,77,55],
        "Engeneering":[81,85,77,75,66]
    }
}
dict['Roll Number']=["1MV21EE007","1CD21CS194","1MV21EE008","1MV21EE009","1MV21EE010"]
print(dict)
print(dict["marks"]["Puc"])
print(dict.keys())
print(dict.values())
#Set is unordered collection of items each element in the set is unique and non duplicate
dic={
    "table":["a piece of furniture","list of facts and figures"],
    "cat":"a small animal"

}
print(dic["table"])
sets={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(sets))
dict={}
subject=input("Enter the subject name:")
marks=int(input("Enter the marks:"))
dict[subject]=marks
subject2=input("Enter the second sub name:")
marks2=int(input("Enter the second sub marks:"))
dict[subject2]=marks2
subject3=input("Enter the 3rd sub name:")
marks3=int(input("Enter the 3rd sub marks:"))
dict[subject3]=marks3
print(dict)