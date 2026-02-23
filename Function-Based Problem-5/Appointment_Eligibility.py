def check_patient_eligibility(age):
    if age >= 18:
        status = "Eligible"
    else:
        status = "Not Eligible"

    print("Patient Age:", age)
    print("Eligibility Status:", status)
check_patient_eligibility(21)