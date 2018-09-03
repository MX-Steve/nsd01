public class Hello { //定义一个程序类
	public static void main(String arg[]){
		System.out.println("Hello World!");
		/*
			尽量少用！
		
		int num = 10;
		System.out.println(num * 2);
		int maxValue=Integer.MAX_VALUE;
		int minValue=Integer.MIN_VALUE;
		System.out.println(maxValue);
		System.out.println(minValue);
		System.out.println(maxValue+1);
		long result = maxValue + 1L;
		long re = (long)maxValue +1; #强制类型转换，小转大无所谓，大转小，可能损失精度
		System.out.println(result);
		System.out.println(re);
		long num1 = 2147483648L;
		在变量声明的时候设置默认值
		
		double num = 10.2;
		System.out.println(num * 2);
		float f1 = 1.1f;
		System.out.println(f1);
		int n1 = 10;
		int n2 = 4;
		System.out.println(n1/n2);
		System.out.println(n1/(float)n2);
		*/
		char c = 'A';
		System.out.println(c);
		int a = c;
		System.out.println(a);
	}
}