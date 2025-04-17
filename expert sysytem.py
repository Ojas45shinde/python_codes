import sys
import tkinter as tk
from tkinter import messagebox 
 

def diagnose(symptoms):
    """EXPERT SYSTEM FOR DISEASES DIAGNOSIS BASED ON INPUTS SYMPTOMS"""

    if "unexplained weight loss" in symptoms and "fatigue" in symptoms and "persistent cough" in symptoms:
        return("possible early_stage lung cancer. Please consult an oncologist")

    elif "Frequent urination" in symptoms and "excessive thirst" in symptoms and "unexplained weight loss" in symptoms:
        return("possible diabetes.Please consult an ") 

    elif "Chest pain" in symptoms and "Shortness of breath" in symptoms and "dizziness" in symptoms:
        return("possible heart disease")

    elif "Persistent headache" in symptoms and "Blurred vision" in symptoms and "Nausea" in symptoms:
        return("possible brain tumor")

    elif "joint pain" in symptoms and "swelling" in symptoms and "stiffness" in symptoms:
        return("possible arthritis") 

    elif "Abdominal pain" in symptoms and "Nausea" in symptoms and "Vomiting" in symptoms:
        return("possible Gastritis or food poisoning.")     

    elif "High fever" in symptoms and "Severe headache" in symptoms and "Stiff neck" in symptoms:
        return("possible meningitis")   

    else:
        return("Symptoms do not match.a specific condition.Please consult a generic physician. ")

def get_diagnosis():
    symptoms_input=entry.get()
    symptoms_list=[sym.strip().lower() for sym in symptoms_input.split(',')]
    diagnosis=diagnose(symptoms_list)
    messagebox.showinfo("diagnosis result:",diagnosis)

root =tk.Tk()
root.title("Medical Expert System")
root.geometry("400x300")     
label=tk.Label(root,text="Enter your symptoms seperated by commas:")
label.pack(pady=10)
entry=tk.Entry(root,width=50)
entry.pack(pady=5)
button=tk.Button(root,text="Diagnosis",command=get_diagnosis,font=("Arial",14),bg='lightblue')
button.pack(pady=20)
root.mainloop()
