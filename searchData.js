var results = [];
var searchField = "name";
var searchVal = "my Name";
for (var i=0 ; i < obj.list.length ; i++)
{
    if (obj.list[i][searchField] == searchVal) {
        results.push(obj.list[i]);
    }
}