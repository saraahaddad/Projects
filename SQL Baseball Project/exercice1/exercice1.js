$( document ).ready(function() {
    $( "#lancer" ).click(function() {
        var annee = $('#annee').val();
        poste('b.nameLast as Nom, b.nameFirst as Prenom, a.teamID as teamID, a.salary as salary \
                FROM Salaries as a \
                INNER JOIN Master as b \
                ON a.playerID = b.playerID \
                WHERE a.salary = (SELECT max(salary) FROM Salaries WHERE yearID=' + annee + ') and a.yearID=' + annee);
    });
    
    function genereTableau(donnees, id){
        var nb = donnees.length;
        if(nb>0){
            var nbattributs = donnees[0].length;
            var htmltable="<tr>";
            for(var attr in donnees[0]){
                htmltable=htmltable+"<th>"+attr+"</th>";
            };
            htmltable=htmltable+"</tr>";
            for(var x=0;x<nb;x++){
                htmltable=htmltable+"<tr>";
                for(var a in donnees[x]){
                    htmltable=htmltable+"<td>"+donnees[x][a]+"</td>";
                }
                htmltable=htmltable+"</tr>";
            }
            $("#"+id).html(htmltable);
        }else{
            alert("Le résultat retourné est vide.");
            $("#"+id).html("");
        }
    }
    
    function poste(requete){
        var postData = {};
        postData["db"] = "dift6800_baseball";
        postData["query"] = requete;
    //La requête AJAX suit, faisant appel au backend db.php qui se trouve dans le même répertoire
        $.post(
            "http://www-ens.iro.umontreal.ca/~dift6800/baseball/db.php",
            postData,
            function(reponse,status){
            console.log(reponse.data);
            var obj = JSON.parse(reponse);
            if(obj.error==""){  
                genereTableau(obj.data, "table");
            }else{
            alert("Erreur:"+obj.error);
            }
            }
        );
    };
});