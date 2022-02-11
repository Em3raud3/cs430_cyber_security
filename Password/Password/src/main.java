// ?  Author: Jeffrey Weng

// ? Useage:
// ? 		Run the program
// ? 		Enter file name of dictionary as instructed
// ? 		Enter file name of password file as instructed

import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;

public class main{
    public static void main(String[] args)

    {   // ! Load in the wordlist in set for fast lookup time
        // User input for file name
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter the name of the file you would like to use: ");
        String dictionaryName = input.nextLine();
        Set<String> word = new LinkedHashSet<String>();

        // !Read file into word line by line
        try {
            Scanner file = new Scanner(new File(dictionaryName));
            while (file.hasNextLine()) {
                word.add(file.nextLine());
            }
            file.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }

        // ! Load in user information
        List <String> user = new ArrayList<String>();
        try {
            System.out.println("Please enter in name of user information file");
            String fileName = input.nextLine();
            Scanner file = new Scanner(new File("fileName"));
            while (file.hasNextLine()) {
                user.add(file.nextLine());
            }
            file.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        }

        //close the scanner
        input.close();

        // ? Create a List of List of strings
        List<List<String>> userInfoArray = new ArrayList<List<String>>();

        // ? Loop over array and split string with : as delimiter
        for (int i = 0; i < user.size(); i++) {
            String[] userInfo = user.get(i).split(":");
            userInfoArray.add(Arrays.asList(userInfo));
        }



        // ? Create Array List holding only relevant info
        ArrayList<ArrayList<String>> parsedData = new ArrayList<ArrayList<String>>();

        ArrayList<String> passwordList = new ArrayList<String>(); // * This is mainly used as a counter for how many passwords was I able to crack

        // Start a timer
        long startTime = System.nanoTime();

        for (int i = 0; i < userInfoArray.size(); i++) {
            // split index  5 with space as delimiter of the 4 index of userInfoArray
            String[] nameData = userInfoArray.get(i).get(4).split(" ");
            parsedData.add(new ArrayList<String>(Arrays.asList(nameData)));
            parsedData.get(i).add(userInfoArray.get(i).get(1).substring(0,2)); // * Added Salt
            parsedData.get(i).add(userInfoArray.get(i).get(1)); // * Added Encrypted Password
        }
        // * [firstName, lastName, Salt, Encrypted Password]

        // * Loop though nameData and begin to crack password
        for (int i = 0; i < parsedData.size(); i++) {
            //! Try firstname
            mangleWord(parsedData.get(i).get(0), parsedData.get(i).get(2), parsedData.get(i).get(3), i + 1, passwordList);

            //! Try lastname
            mangleWord(parsedData.get(i).get(1), parsedData.get(i).get(2), parsedData.get(i).get(3), i + 1, passwordList);

            //! Try wordList
            for (String wordList : word) {
                mangleWord(wordList, parsedData.get(i).get(2), parsedData.get(i).get(3), i + 1, passwordList);
            }
        }
        // Print out length of passwordList
        System.out.println(passwordList.size() + " out of 20 passwords found");

        // End the timer
        long endTime = System.nanoTime();

        // Print out the time it took to run the program
        System.out.println("Time: " + (endTime - startTime) / 1000000000.0 + " seconds");

    }

    // ! This methods tries different mangling of the word and checks if it matches the encrypted password
    public static void  mangleWord(String word, String salt, String encryptedPassword, int index, ArrayList<String> passwordList) {

        if (jcrypt.crypt(salt, word).equals(encryptedPassword)) {
            System.out.println("Password " + index + " Cracked: " + word + " ==> " + encryptedPassword); // * Try word as it is
            passwordList.add(word);
        }

        else if (jcrypt.crypt(salt, word.substring(0, word.length() - 1)).equals(encryptedPassword)) {  // * Try to remove last letter
            System.out.println("Password " + index + " Cracked: " + word.substring(0, word.length() - 1) + " ==> " + encryptedPassword);
            passwordList.add(word.substring(0, word.length() - 1));
            return;
        }

        else if (jcrypt.crypt(salt, repeat(word)).equals(encryptedPassword)) {  // * Try repeating word
            System.out.println("Password " + index + " Cracked: " + repeat(word) + " ==> " + encryptedPassword);
            passwordList.add(repeat(word));
            return;
        }
        else if (jcrypt.crypt(salt, reverse(firstLetterCap(word.substring(0, word.length() - 1)))).equals(encryptedPassword)) {  // * First letter cap, reverse, and remove last letter
            System.out.println("Password " + index + " Cracked: " + reverse(firstLetterCap(word.substring(1))) + " ==> " + encryptedPassword);
            passwordList.add(reverse(firstLetterCap(word.substring(1))));
            return;
        }

        else if (jcrypt.crypt(salt, repeatReverse(word)).equals(encryptedPassword)) {  // * Try repeating word
            System.out.println("Password " + index + " Cracked: " + repeatReverse(word) + " ==> " + encryptedPassword);
            passwordList.add(repeatReverse(word));
            return;
        }

        else if (jcrypt.crypt(salt, word.toUpperCase()).equals(encryptedPassword)) {  // * Try All Capital
            System.out.println("Password " + index + " Cracked: " + word.toUpperCase() + " ==> " + encryptedPassword);
            passwordList.add(word.toUpperCase());
            return;
        }

        else if (jcrypt.crypt(salt, reverse(firstLetterCap(word))).equals(encryptedPassword)) {  // * Try first letter capital + reverse
            System.out.println("Password " + index + " Cracked: " + reverse(firstLetterCap(word)) + " ==> " + encryptedPassword);
            passwordList.add(reverse(firstLetterCap(word)));
            return;
        }

        else if (jcrypt.crypt(salt, repeat(word + reverse(word))).equals(encryptedPassword)) {  // * Try repeating a reversed word
            System.out.println("Password " + index + " Cracked: " + word + reverse(word) + " ==> " + encryptedPassword);
            passwordList.add(word + reverse(word));
            return;
        }

        else if (jcrypt.crypt(salt, firstLower(word)).equals(encryptedPassword)) {  // * only first lower case
            System.out.println("Password " + index + " Cracked: " + firstLower(word) + " ==> " + encryptedPassword);
            passwordList.add(firstLower(word));
            return;
        }

        else if (jcrypt.crypt(salt, word.substring(1)).equals(encryptedPassword)) {  // * Try to remove first letter
            System.out.println("Password " + index + " Cracked: " + word.substring(1) + " ==> " + encryptedPassword);
            passwordList.add(word.substring(1));
            return;
        }

        else if (jcrypt.crypt(salt, firstLetterCap(word)).equals(encryptedPassword)) {
            System.out.println("Password " + index + " Cracked: " + word.toLowerCase() + " ==> " + encryptedPassword); // * Try first letter capitalized
            passwordList.add(word.toLowerCase());
        }

        else if (jcrypt.crypt(salt, word.toLowerCase()).equals(encryptedPassword)) {
            System.out.println("Password " + index + " Cracked: " + word.toLowerCase() + " ==> " + encryptedPassword); // * Try to all lower case
            passwordList.add(word.toLowerCase());
            return;
        }

        else if (jcrypt.crypt(salt, reverse(word.toLowerCase())).equals(encryptedPassword)) {
            System.out.println("Password " + index + " Cracked: " + reverse(word.toLowerCase()) + " ==> " + encryptedPassword); // * tries an all lowercase word that is reversed
            passwordList.add(reverse(word.toLowerCase()));
            return;
        }

        else{
            appendPrepend(word, salt, encryptedPassword, index, passwordList); // * Try to add letter to start and end
            appendPrepend(firstLower(word), salt, encryptedPassword, index, passwordList); // * only first letter lower and try to prepend/append
            appendPrepend(word.substring(0, word.length() - 1), salt, encryptedPassword, index, passwordList); // * Remose last letter and add random letter
        }
    }

    public static void appendPrepend(String word, String salt, String encryptedPassword, int index, ArrayList<String> passwordList){
        for (int j= 32; j < 127; j++) {
            if(jcrypt.crypt(salt, word + String.valueOf((char) j)).equals(encryptedPassword)){
                System.out.println("Password " + index + " Cracked: " + (word + String.valueOf((char) j)) + " ==> " + encryptedPassword);
                passwordList.add(word + String.valueOf((char) j));
                break;
            }
            else{
                if(jcrypt.crypt(salt, String.valueOf((char) j) + word).equals(encryptedPassword)){
                    System.out.println("Password " + index + " Cracked: " + (String.valueOf((char) j) + word) + " ==> " + encryptedPassword);
                    passwordList.add(String.valueOf((char) j) + word);
                    break;
                }
            }
        }
    }

    public static String reverse(String input) {

        if (input == null) {
            return input;
        }

        String output = "";

        for (int i = input.length() - 1; i >= 0; i--) {
            output = output + input.charAt(i);
        }

        return output;
    }

    public static String repeat(String input) {

        if (input == null) {
            return input;
        }

        String output = input;

        output += output;

        return output;
    }
    public static String repeatReverse(String input) {

        if (input == null) {
            return input;
        }

        String output = input;

        output = reverse(input) + output;

        return output;
    }

    public static String firstLetterCap(String str) {
        if(str == null || str.isEmpty()) {
            return str;
        }

        return str.substring(0, 1).toUpperCase() + str.substring(1).toLowerCase();
    }

    public static String firstLower(String str) {
        if(str == null || str.isEmpty()) {
            return str;
        }

        return str.substring(0, 1).toLowerCase() + str.substring(1).toUpperCase();
    }


}

        // Example


        //* michael   Normal
        //* liagiba   abigail (flipped)
        //* amazing   Normal
        //* eeffoc    coffee (flipped)
        //* squadro   squadron (missing n)
        //* icious    Vicious (Missing V)
        //* abort6    added 6
        //* rdoctor   docter (added r)
        //* doorrood  repeat reversed
        //* keyskeys  repeat
        //* Impact    Impact (I capatalized)
        //* sATCHEL   Satchel (Only s not Capito)s
        //* THIRTY    All Caps
        //* teserP    Preset reversed and added cap
        //* sHREWDq   Shrewd (Added q and different caps)
        //* enoggone  gone forward and backward
        //* obliqu3   Oblique (Added 3)
        //* litpeR    Reptile
        //* Salizar   Last name
        //* hI6d$pC2  Random