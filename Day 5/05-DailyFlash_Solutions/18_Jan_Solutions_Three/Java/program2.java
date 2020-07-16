
import java.io.*;

class Thrashing {
	public static void main(String ... kbd) throws IOException {

		int n = 0;
		System.out.printf("Total Numbers : ");
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		try {
			n = Integer.parseInt(br.readLine());
		}
		catch (NumberFormatException ne){
			System.out.printf("Not a Number\n");
		}

		if(n <= 0 )
			System.exit(0);

		System.out.printf("Sum : %d\n", n*(n + 1)/2);
	}	
}
