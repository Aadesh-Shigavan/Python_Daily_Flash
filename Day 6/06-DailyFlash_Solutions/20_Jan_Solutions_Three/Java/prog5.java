class Demo{
	public static void main(String[] args){
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				System.out.print(i % 2 == 0 ? "0 " : "1 ");
			}	
			System.out.println();
		}		
	}
}
