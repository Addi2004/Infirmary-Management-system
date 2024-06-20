import streamlit as st
import _mysql_connector
from datetime import datetime
from maintry2working import InfirmaryManagementSystem, InvalidPasswordException



@st.cache(allow_output_mutation=True)
def create_infirmary_system():
    return InfirmaryManagementSystem()


def main():
    st.title("Infirmary Management System")

    infirmary_system = create_infirmary_system()

    user_type = st.sidebar.selectbox("Choose your user type:", [
                                     "Patient", "Doctor", "Manager"])

    if user_type == "Patient":
        patient_menu(infirmary_system)
    elif user_type == "Doctor":
        doctor_menu(infirmary_system)
    elif user_type == "Manager":
        manager_menu(infirmary_system)


def patient_menu(infirmary_system):
    st.subheader("Patient Menu")
    patient_action_choice = st.selectbox("Choose an action:", [
                                         "Buy Medicine", "Book Appointment", "Display All Products"])

    if patient_action_choice == "Buy Medicine":
        buy_medicine(infirmary_system)
    elif patient_action_choice == "Book Appointment":
        book_appointment(infirmary_system)
    elif patient_action_choice == "Display All Products":
        infirmary_system.displayAllProducts()


def buy_medicine(infirmary_system):
    st.subheader("Buy Medicine")
    product_id = st.number_input("Enter the Product ID to buy:")
    quantity_to_buy = st.number_input(
        "Enter the quantity to buy:", min_value=1)
    if st.button("Buy"):
        infirmary_system.sellProduct(product_id, quantity_to_buy)
        st.success(f"Bought {quantity_to_buy} of Product ID {product_id}")


def book_appointment(infirmary_system):
    st.subheader("Book Appointment")
    roll_no = st.text_input("Enter your Roll No.:")
    sap_id = st.text_input("Enter your SAP ID:")
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0)
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
    category_choice = st.selectbox("Select doctor category:", [
                                   "General Illnesses", "Injuries"])
    if category_choice == "General Illnesses":
        available_doctors = ["Dr. John", "Dr. Mary"]
    else:
        available_doctors = ["Dr. Smith", "Dr. Johnson"]
    selected_doctor = st.selectbox("Select doctor:", available_doctors)
    appointment_time = st.text_input(
        "Enter appointment time (YYYY-MM-DD HH:MM):")
    if st.button("Book Appointment"):
        infirmary_system.addAppointment(
            selected_doctor, sap_id, appointment_time)
        infirmary_system.addPatient(
            roll_no, sap_id, name, age, gender, selected_doctor)
        st.success(f"Appointment booked with {selected_doctor} at {appointment_time}")
        # Add the appointment directly using the backend method
        infirmary_system.addAppointment(
            selected_doctor, sap_id, appointment_time)


def doctor_menu(infirmary_system):
    st.subheader("Doctor Menu")
    doctor_action_choice = st.selectbox(
        "Choose an action:", ["View My Appointments", "View Patient Details"])

    if doctor_action_choice == "View My Appointments":
        doctor_name = st.text_input("Enter your name:")
        appointments = infirmary_system.displayAppointments(doctor_name)
        if appointments:
            st.write("Your appointments:")
            for appointment in appointments:
                st.write(f"Patient: {appointment[0]} | Time: {appointment[1]}")
        else:
            st.write("No appointments found.")
    elif doctor_action_choice == "View Patient Details":
        patient_id = st.text_input("Enter patient SAP ID:")
        infirmary_system.displayPatientDetails(patient_id)


def manager_menu(infirmary_system):
    st.subheader("Manager Menu")
    manager_password = st.text_input("Enter manager password:")
    if manager_password == "managerPassword":
        manager_action_choice = st.selectbox("Choose an action:", [
                                             "Update Stock", "Display All Products"])

        if manager_action_choice == "Update Stock":
            infirmary_system.manageStock(manager_password)
        elif manager_action_choice == "Display All Products":
            infirmary_system.displayAllProducts()
    elif manager_password:
        st.error("Invalid manager password")


if __name__ == "__main__":
    main()
