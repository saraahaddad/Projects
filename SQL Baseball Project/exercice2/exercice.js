//Ces fonctions sont prises de la demo 9, et permettent d'afficher la requete SQL dans un tableau

$(document).ready(function(){
    $("#lancer").click(function(){
        poste('CONCAT(Master.nameFirst," ",Master.nameLast) as NomComplet,Pitching.G,Pitching.W,Pitching.SV,W+SV,Pitching.L,Pitching.SO,Pitching.H,Pitching.BB,Pitching.IPouts,Salaries.salary as Salaire \
        FROM Salaries INNER JOIN Pitching ON Salaries.playerID=Pitching.playerID INNER JOIN Master ON Salaries.playerID=Master.playerID \
        WHERE(Pitching.teamID="MON")AND(Pitching.yearID=1996)AND(Salaries.teamID="MON")AND(Salaries.yearID=1996)AND(Pitching.GS=0) \
        ORDER BY (Pitching.W+Pitching.SV) DESC');
    });
    })

function poste(requete){
    var postData = {};
    postData["db"] = "dift6800_baseball";
    postData["query"] = requete;	
    $.post(
      "http://www-ens.iro.umontreal.ca/~dift6800/baseball/db.php",
      postData,
      function(reponse,status){
         console.log(status);
         var obj = JSON.parse(reponse);
        if(obj.error==""){  
            genereTableau(obj.data, "table");
        }else{
          alert("Erreur:"+obj.error);
        }
      }
    );
};
function genereTableau(donnees, id){
    var nb = donnees.length;
    if(nb>0){
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
        alert("La réponse à la requête est vide.");
        $("#"+id).html("");
    }
};
