namespace Final;
using System;
using System.Linq;
using System.Collections.Generic;
class Program
{
       // hardcode employee's username and password for login authencation
    static Dictionary<string, string> dict_login = new Dictionary<string, string>();
            //create a dictionary of available room categories
    static Dictionary<string, double> dict_aRooms = new Dictionary<string, double>();
    //create a dictionary of reserved rooms
    static Dictionary<string, double> dict_rRooms = new Dictionary<string, double>();
    //create a dictionary of food sides
    static Dictionary<string, double> dict_sides = new Dictionary<string, double>();
    static void Main(string[] args)
    {
        //Login
        dict_login.Add("Alice","123");
        Rooms();

        Console.WriteLine("CIDM2315 Final Project: Eric Starks");
        Console.WriteLine("Welcome to Buff Hotel");

        //if login is successful show these
        bool login_result = employee_login(dict_login);
        if(login_result){
            Console.WriteLine("*******************");
            Console.WriteLine("Please select: ");
            Console.WriteLine("1. Show Avaible Rooms");
            Console.WriteLine("2. Check-In");
            Console.WriteLine("3. Show Reserved Rooms");
            Console.WriteLine("4. Check-Out");
            Console.WriteLine("5. Log-Out");
            Console.WriteLine("*******************");

            // Choose where you want to go 
            string choice = Console.ReadLine();
            if(choice == "1"){
                ShowR(dict_aRooms);
            }
            
        }

    }
        
    
    public static bool employee_login(Dictionary<string, string> dict_login){
        // input username and password
        Console.WriteLine("Please input username");
        string username = Console.ReadLine();
        
        Console.WriteLine("Please input password");
        string password = Console.ReadLine();

        if(dict_login.ContainsKey(username)){
            if (dict_login[username] == password){
                Console.WriteLine("Login Successfully.\n");
                Console.WriteLine($"** Hello Cashier: {username} **");

                return true;
            }else{
                Console.WriteLine("Wrong Password");
                return false;
            }
        }
        else{
                Console.WriteLine("User does not exit.");
                return false;
        }
    }
//creating-showing rooms
    public static void Rooms(){

        dict_aRooms.Add("Room number: 101; Capacity:", 2);
        dict_aRooms.Add("Room number: 102; Capacity:", 2);
        dict_aRooms.Add("Room number: 103; Capacity:", 2);
        dict_aRooms.Add("Room number: 104; Capacity:", 2);
        dict_aRooms.Add("Room number: 105; Capacity:", 2);
        dict_aRooms.Add("Room number: 106; Capacity:", 2);
}

   public static void ShowR(Dictionary<string, double> dict_aRooms){
        int R = 0;
        foreach(var Rooms in dict_aRooms){
            Console.WriteLine($"{Rooms.Key}\t {Rooms.Value}");
            R++;
        }
}
}
