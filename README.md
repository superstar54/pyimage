###pyliterature
A Python to fetch definitions from cambridge ditionary.



###Author
* Xing Wang  <xingwang1991@gmail.com>



###Dependencies

* Python >=27
* beautifulsoup4
* spynner (optional)
* nltk (optional)



####Examples

```python
>>> from pycambtionary import Pycambtionary
>>> word = 'love'
>>> mydict = Pycambtionary(word)
>>> mydict.parser()
>>> jsonword = mydict.get_jsonword()
>>> print(jsonword)
{
    "love": {
        "noun": [
            "the feeling of liking another adult very much and being romantically and sexually attracted to them, or strong feelings of liking a friend or person in your family: ",
            "a person that you love and feel attracted to: ",
            "used as a friendly form of address: ",
            "used before your name at the end of letters, cards, etc. to friends or family: ",
            "to love someone in a romantic and sexual way: ",
            "to start to love someone romantically and sexually: ",
            "strong liking for: ",
            "something that you like very much: ",
            "(in tennis) the state of having no points: "
        ],
        "verb [ T ]": [
            "to like another adult very much and be romantically and sexually attracted to them, or to have strong feelings of liking a friend or person in your family: ",
            "to like something very much: ",
            "used, often in requests, to say that you would very much like something: "
        ]
    }
}
```

If you want to add features/improvement or report issues, feel free to send a pull request!


###TODO
* add database
* change 'verb [ T ]'  to 'verb'
* fetch example, ldiom
* fetch synonyms and related words
* returns the infinitive form of a word, like give for gave
