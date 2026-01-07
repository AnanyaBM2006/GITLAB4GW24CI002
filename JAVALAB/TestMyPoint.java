package p4;

public class MyPoint {
	private int x;
	private int y;
	public MyPoint() {
		this.x=0;
		this.y=0;
	}
	public MyPoint(int x,int y) {
		this.x=x;
		this.y=y;
	}
	
	public void setXY(int x,int y) {
		this.x =x;
		this.y =y;
	}
	public int[] getXY() {
		 return new int[] {x,y};
		 
	}
	public String toString() {
		return "("+x+","+y+")";
		
	}
	
	public double distance(int x,int y) {
		int dx = this.x-x;
		int dy = this.y-y;
		return Math.sqrt(dx*dx + dy*dy);
	}
	
	public double distance(MyPoint another) {
		int dx =this.x-another.x;
		int dy =this.y-another.y;
		return Math.sqrt(dx*dx +dy*dy);
		
		
	}
	
	public double distance() {
		return Math.sqrt(x*x+y*y);
				
	}
    }

 class TestMyPoint{
	public static void main(String[] args) {
		MyPoint p1= new MyPoint();
		MyPoint p2= new MyPoint(3,4);
		System.out.println("p1:"+p1);
		System.out.println("p2:"+p2);
		p1.setXY(5, 6);
		System.out.println("After setXY,p1:"+p1);
		
		int[] coords = p1.getXY();
		System.out.println("p1 x:" + coords[0]+",y:"+coords[1]);
		double d1 = p1.distance(4, 6); 
		System.out.println("Distance from p1 to (4,6): " + d1); 
		double d2 = p1.distance(p2); 
		System.out.println("Distance from p1 to p2: " + d2);
		double d3 = p2.distance();
		System.out.println("Distance from p2 to origin: " + d3);
		
		// TODO Auto-generated method stub

	}

}
