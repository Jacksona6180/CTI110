
public class M6PE1_JacksonAshley

{
    public static void main(String[] args)
    {
	    float tractSize,acres;
	    int SQ_FEET_PER_ACRE = 43560;
    }

	{
            System.out.print("Enter the number of square feet in the tract: ");
	}
        {
            Scanner obj=new Scanner(System.in);
		tractSize = obj.nextFloat(); //reading input from user
		acres = tractSize/ SQ_FEET_PER_ACRE; //calculating acres.
		System.out.println("The size of the tract is "+acres+" acres.");
	}
}

