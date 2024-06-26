# Tkinter
Tkinter is the most commonly  used library for developing GUI (Graphical User Interface) in Python.
I give some basic practice codes for learn tkinter
<h3>Miles_to_kilometers</h3> 

![image](https://github.com/LeepyShah/Tkinter/assets/158757009/98643485-477b-417d-b073-3d0767ad7e16)
<h6>After click on Convert button</h6> 

![image](https://github.com/LeepyShah/Tkinter/assets/158757009/16771fce-b290-4dff-a83c-08740250a0ac)

<h3>basic_window</h3> 

![image](https://github.com/LeepyShah/Tkinter/assets/158757009/7bc7ff6d-7af2-423e-9495-5687538dde11)

<h3>widgets_update</h3>

![image](https://github.com/LeepyShah/Tkinter/assets/158757009/e75b4a42-3bd5-410c-8001-390a7cae4611)

<pre>
<b>Widgets can be updated with config</b> 
  
  Ex.Label.config(text="some new text")
     Label['text']='some new text'
  
</pre>
<h3>Tkinter Variables</h3>
<pre>
  -->Tkinter has inbuilt variabels that are designed to work  with widgets
  -->They are automatically updated by a widget and they update a widget
  -->Although they still store basic data like integers,strings & boolean
</pre> 
<h4>tkinter_var</h4>

![image](https://github.com/LeepyShah/Tkinter/assets/158757009/9e41e486-8119-4ff3-9efe-f2b05b5ff617)

![image](https://github.com/LeepyShah/Tkinter/assets/158757009/7349a119-8be7-465d-8744-2f1fdee28040)

<b>After clicking button </b>

![image](https://github.com/LeepyShah/Tkinter/assets/158757009/b43eabfd-35a3-48a3-8110-69c2e32ae140)

<h3>Buttons</h3><br>
There are 3 major kind of buttons<br>
<pre>
1.Button
2.Checkbutton
3.Radiobutton
</pre>
But to use them properly you need tkinter variabels
<h3>buttons.py</h3>

![image](https://github.com/LeepyShah/Tkinter/assets/158757009/7149fb3b-0121-4b94-ae00-0f72f2dce95b)

<h3>Functions with arguments <sub>(inside a button)</sub></h3>
<p>We already solve this !</p>
Command=lambda:print('argument')<br>
Alternatively ,you can also create a function that retruns another function
<h3>fun_with_argument.py</h3>

![image](https://github.com/LeepyShah/Tkinter/assets/158757009/4fac4b53-febc-4814-885f-7cf1263d394b)

After clicking button output in terminal is

![image](https://github.com/LeepyShah/Tkinter/assets/158757009/e171c43f-1e3c-49e4-af0a-7b05692ff679)

<h3>Event Binding</h3>
Events can be lots of things<br>
<br>
 Keyword inputs<br>
 Widgets can be changed<br>
 Widgets can be selected/Unselected<br>
 Mouse click/motion/wheel<br>
<br>
These event can be observed and used<br>
Eg.Run a function on a button press<br><br>
You need to bind events to a widget<br>
Eg. Widget.bind(event,function)<br>
<br>
<h4>Format:</h4>modifier-type-detail<br>
                 Alt-Keypress-a<br>
<h5>link for reference</h5>            
[Link Text]("https://www.pythontutorial.net/tkinter/tkinter-event-binding/")




