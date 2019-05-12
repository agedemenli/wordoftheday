# wordoftheday
Meet the word of the day. This API gives you the word of the day with its meaning, in any of the supported languages.
The respond you get will, of course, differ every day.

You need no secret keys etc.
You can run it on your local machine just like:

`python3 manage.py runserver`

Test it on your browser like :

`http://localhost:8000/randomword/en`

You can, of course, add more words and languages if you want.

### Usage

`randomword/en`
```json
{
	"word": "Efficient",
	"definition": "Achieving maximum productivity with minimum wasted effort or expense."
}
```

`randomword/tr`
```json
{
	"word": "Niyet",
	"definition": "Bir şeyi yapmayı önceden isteyip düşünme, maksat."
}
```
`randomword/aq`
```
NO SUCH LANGUAGE AVAILABLE
```
