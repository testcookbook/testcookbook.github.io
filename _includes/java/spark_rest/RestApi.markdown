```java
import static spark.Spark.*;

public class RestApi {
    public static void main(String[] args) {
        get("/", (req, res) -> "Root Route");
        get("/hello", (req, res) -> "Hello World");
    }
}
```