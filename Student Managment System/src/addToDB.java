
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;


public class addToDB {


	public static int enterData(Student st) {
		
		try {
			
			PreparedStatement q = databseUtility.getConnection().prepareStatement("insert into details values(?,?,?,?,?,?,?,?,?,?,?,?,?)");
			q.setString( 1,st.getName());
			q.setInt( 2,st.getRegNo());
			q.setString(3, st.getdOB());
			q.setInt(4,st.getAge());
			q.setString(5,st.getDept());
			q.setString(6,st.getFatherName());
			q.setString(7,st.getMotherName());
			q.setString(8,st.getContactNumber());
			q.setString(9,st.geteMail());
			q.setString(10,st.getAddress());
			q.setString(11,st.getBloodGrp());
			q.setString(12,st.getAdmissionDate());
			q.setString(13,st.getYearOfPass());
			int res = q.executeUpdate();
			return res;
		}
		catch(Exception e) {
			e.printStackTrace();
		}
		return 0;
	}
	
	public static void getData(int regNo) throws SQLException {
		PreparedStatement q = databseUtility.getConnection().prepareStatement("select * from details where regNo = ?");
		q.setInt(1, regNo);
		ResultSet res = q.executeQuery();
		
		while(res.next()) {
			System.out.println("Name: "+res.getString("Name"));
			System.out.println("Reg No: "+res.getInt("Regno"));
			System.out.println("DOB: "+res.getString("DOB"));
			System.out.println("Age: "+res.getInt("Age"));
			System.out.println("Department: "+res.getString("Department"));
			System.out.println("Father_Name: "+res.getString("Father_Name"));
			System.out.println("Mother_Name: "+res.getString("Mother_Name"));
			System.out.println("Contact: "+res.getString("Contact"));
			System.out.println("Email: "+res.getString("Email"));
			System.out.println("Address: "+res.getString("Address"));
			System.out.println("Blood: "+res.getString("Blood"));
			System.out.println("DOA: "+res.getString("DOA"));
			System.out.println("Graduation_Year: "+res.getString("Graduation_Year"));
			

		}
	
	}
	public static int removeData(int regNo) throws SQLException{
		PreparedStatement q = databseUtility.getConnection().prepareStatement("delete from details where regNo = ?");
		q.setInt(1, regNo);
		int res = q.executeUpdate();
		return res;
	}
}
