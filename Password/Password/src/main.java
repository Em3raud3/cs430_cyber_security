import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;

public class main{
    public static void main(String[] args)

    {   // ! Load in the wordlist in set for fast lookup time
        String dictionaryName = "wordlist.txt";
        Set<String> word = new LinkedHashSet<String>();

        // Read file into word line by line
        try {
            Scanner file = new Scanner(new File(dictionaryName));
            while (file.hasNextLine()) {
                word.add(file.nextLine());
            }
            file.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }

        // Print out the word
        // System.out.println(word);

    }
}