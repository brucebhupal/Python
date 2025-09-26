Module Module1
    Sub main(args As String())
        Console.BackgroundColor = ConsoleColor.DarkBlue
        Console.WriteLine("press any key to start")
        Console.ReadKey()
        Console.Clear()

        For y = 1 To 10
            Console.WriteLine()
        Next y

        Console.WriteLine("/-\")
        Console.WriteLine("| |")
        Console.WriteLine("| |")
        Console.WriteLine("|B|")
        Console.WriteLine("|R|")
        Console.WriteLine("|U|")
        Console.WriteLine("|C|")
        Console.WriteLine("|E|")
        Console.WriteLine("/ \")

        For x = 600 To 20 Step -20

            If x > 550 Then
                Console.WriteLine("...")
            Else
                Console.WriteLine()
            End If
            Threading.Thread.Sleep(x)
        Next x
    End Sub

End Module
