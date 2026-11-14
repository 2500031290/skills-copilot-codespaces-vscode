/** A small console example for practicing with Copilot. */
public class Main {
    static String greeting(String name) {
        String cleanName = name == null || name.isBlank() ? "learner" : name.trim();
        return "Hello, " + cleanName + "! Welcome to Copilot Skills Lab.";
    }

    public static void main(String[] args) {
        System.out.println(greeting("Java learner"));
    }
}
