public class Student {
    private String name;

    public Student(String n) {
        this.name = n;
    }

    public void greet() {
        System.out.println("Hello, " + name);
    }

    public static void main(String[] args) {
        Student s = new Student("Vedant");
        s.greet();
    }
}
