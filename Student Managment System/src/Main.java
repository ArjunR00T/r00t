
import java.sql.SQLException;
import java.time.Year;

import java.util.Scanner;

class Student {

	String name;

	int regNo;

	String dOB;

	int age;

	String dept;

	String fatherName;

	String motherName;

	String contactNumber;

	String eMail;

	String address;

	String bloodGrp;

	String admissionDate;

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	String yearOfPass;

	public Student(String name, int regNo, String dOB, String dept, String fatherName, String motherName,

			String contactNumber, String eMail, String address, String bloodGrp, String admissionDate,
			String yearOfPass) {

		super();

		this.name = name;

		this.regNo = regNo;

		this.dOB = dOB;

		this.dept = dept;

		this.fatherName = fatherName;

		this.motherName = motherName;

		this.contactNumber = contactNumber;

		this.eMail = eMail;

		this.address = address;

		this.bloodGrp = bloodGrp;

		this.admissionDate = admissionDate;

		this.yearOfPass = yearOfPass;

		this.age = this.calcAge();

	}

	public String getName() {

		return name;

	}

	public void setName(String name) {

		this.name = name;

	}

	public int getRegNo() {

		return regNo;

	}

	public void setRegNo(int regNo) {

		this.regNo = regNo;

	}

	public String getdOB() {

		return dOB;

	}

	public void setdOB(String dOB) {

		this.dOB = dOB;

	}

	public String getDept() {

		return dept;

	}

	public void setDept(String dept) {

		this.dept = dept;

	}

	public String getFatherName() {

		return fatherName;

	}

	public void setFatherName(String fatherName) {

		this.fatherName = fatherName;

	}

	public String getMotherName() {

		return motherName;

	}

	public void setMotherName(String motherName) {

		this.motherName = motherName;

	}

	public String getContactNumber() {

		return contactNumber;

	}

	public void setContactNumber(String contactNumber) {

		this.contactNumber = contactNumber;

	}

	public String geteMail() {

		return eMail;

	}

	public void seteMail(String eMail) {

		this.eMail = eMail;

	}

	public String getAddress() {

		return address;

	}

	public void setAddress(String address) {

		this.address = address;

	}

	public String getBloodGrp() {

		return bloodGrp;

	}

	public void setBloodGrp(String bloodGrp) {

		this.bloodGrp = bloodGrp;

	}

	public String getAdmissionDate() {

		return admissionDate;

	}

	public void setAdmissionDate(String admissionDate) {

		this.admissionDate = admissionDate;

	}

	public String getYearOfPass() {

		return yearOfPass;

	}

	public void setYearOfPass(String yearOfPass) {

		this.yearOfPass = yearOfPass;

	}

	private int calcAge() {

		int age;

		int year = Year.now().getValue();

		String birthYear = this.dOB;

		birthYear = birthYear.split("/")[2];

		int bY = Integer.parseInt(birthYear);

		age = year - bY;

		return age;

	}

}

public class Main {

	public static void main(String[] args) throws SQLException {

		Scanner sc = new Scanner(System.in);

		while (true) {

			System.out.println("1) Add a new Student");

			System.out.println("2) Get a student details");

			System.out.println("3) Remove a student details");

			System.out.println("Any other option to exit");

			int key = sc.nextInt();

			switch (key) {

			case 1:

				while (true) {
					System.out.println("Enter -1 to Quit\n");

					System.out.println("Enter the name : ");

					String name = sc.next();

					if (name.equals("-1"))
						break;

					System.out.println("Enter the register number : ");

					int regNo = sc.nextInt();

					System.out.println("Enter the date of birth : ");

					String dOB = sc.next();

					System.out.println("Enter the department : ");

					String dept = sc.next();

					System.out.println("Enter the Father Name : ");

					String fatherName = sc.next();

					System.out.println("Enter the Mother Name : ");

					String motherName = sc.next();

					System.out.println("Enter the contact number : ");

					String contactNumber = sc.next();

					System.out.println("Enter the email : ");

					String eMail = sc.next();

					System.out.println("Enter the address : ");

					String address = sc.next();

					System.out.println("Enter the blood group : ");

					String bloodGrp = sc.next();

					System.out.println("Enter the admission date : ");

					String admissionDate = sc.next();

					System.out.println("Enter the year of passing : ");

					String yearOfPass = sc.next();

					Student std = new Student(name, regNo, dOB, dept, fatherName, motherName, contactNumber, eMail,
							address, bloodGrp, admissionDate, yearOfPass);
					
					int res = addToDB.enterData(std);

				}

				break;

			case 2:
				System.out.println("Enter register number");
				int reg = sc.nextInt();
				addToDB.getData(reg);
				System.out.println();
				break;

			case 3:
				System.out.println("Enter register number");
				int reg1 = sc.nextInt();
				int res = addToDB.removeData(reg1);
				if(res == 1) System.out.println("Success");
				else System.out.println("Failed");
				break;

			default:

				return;

			}

		}

	}

}
