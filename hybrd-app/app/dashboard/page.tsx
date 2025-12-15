
"use client";
import React, { useState } from "react";
import { useRouter } from "next/navigation";

// URL de base de votre backend
const API_URL = "http://127.0.0.1:8000"; 


// Composant réutilisable pour les cartes (même celui utilisé précédemment pour la propreté)
const MetricCard = ({ title, value, color, details }) => {
    const colorClasses = {
        green: 'bg-green-100 text-green-700 border-green-500',
        blue: 'bg-blue-100 text-blue-700 border-blue-500',
        orange: 'bg-orange-100 text-orange-700 border-orange-500',
        red: 'bg-red-100 text-red-700 border-red-500',
        default: 'bg-gray-100 text-gray-700 border-gray-500',
    };
    const cardColor = colorClasses[color] || colorClasses.default;

    return (
        <div className={`p-5 rounded-xl shadow-md border-l-4 ${cardColor}`}>
            <p className="text-sm font-medium opacity-80 mb-2">{title}</p>
            <h3 className="text-3xl font-bold mb-1">
                {value}
            </h3>
            <small className="text-xs opacity-80">{details}</small>
        </div>
    );
};


export default function Page() {

    const [inputText, setInputText] = useState("");
    const [summary, setSummary] = useState("");
    const [ton, setTon] = useState("N/A"); // Ajout de valeurs initiales
    const [category, setCategory] = useState("N/A");
    const [score, setScore] = useState("N/A");
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
   
    const router = useRouter();
    const handleLogout = () => {
        localStorage.removeItem("token");
        router.push("/"); 
      };

    // Fonction pour envoyer la requête POST au backend
    const handleAnalysis = async (e) => {
        e.preventDefault();

        if (!inputText.trim()){
            alert("Veuillez entrer du texte à analyser.");
            return;
        }

        setIsLoading(true);
        setError(null);
        setSummary("Analyse en cours..."); 

        try {
            const response = await fetch(`http://127.0.0.1:8000/analyzer`,{
                method: "POST",
                headers: {'Content-Type': 'application/json',},
                body: JSON.stringify({text: inputText})
            });
            
            if (!response.ok){
                throw new Error(`Erreur HTTP: ${response.status} - ${response.statusText}`);
            }

            const data = await response.json();
            console.log(data)
            
            setSummary(data.summary);
            setTon(data.ton);
            setCategory(data.category);
            setScore((data.score * 100).toFixed(1) + "%");

        } catch (err) {
            console.error("Erreur lors de l'analyse:", err);
            setError("Impossible de contacter le serveur d'analyse.");
            setSummary("Échec de l'analyse. " + err.message);
            setTon("ERREUR");
            setCategory("ERREUR");
            setScore("ERREUR");
        } finally {
            setIsLoading(false); 
        }
    }; 


    return (
        <div className="min-h-screen bg-[url('/images/02.jpg')] bg-cover bg-center bg-no-repeat text-white"> 
            
            <header className="bg-black/90 shadow-2xl flex justify-between items-center p-3 py-3">
                <h3 className="ml-20 text-xl font-bold">Dashboard</h3>
                <button className="mr-20 px-4 py-2 bg-red-600 rounded hover:bg-red-700 transition duration-300" onClick={handleLogout}>Logout</button>
            </header>

           
            <div className="max-w-7xl mx-auto p-4 md:p-8">
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">

                    
                    <aside className="lg:col-span-1 bg-black/90 p-8 rounded-xl shadow-2xl h-fit mt-12">
                        <h3 className="text-xl font-semibold mb-4">Texte à Analyser</h3>
                        
                        
                        <form onSubmit={handleAnalysis}>
                            <textarea 
                                className="w-full h-40 p-4 rounded-xl resize-none text-gray-900 border border-gray-700 focus:ring-blue-500"
                                placeholder="Entrez le texte à analyser"
                                value={inputText}
                                onChange={(e) => setInputText(e.target.value)}
                            />
                            <button 
                                type="submit" 
                                className="w-full mt-6 bg-amber-600 hover:bg-amber-700 py-2 rounded font-bold text-white duration-700 disabled:bg-gray-600"
                                disabled={isLoading}
                            >
                                {isLoading ? "Analyse en cours..." : "Soumettre"}
                            </button>
                        </form>
                        {error && <p className="text-red-400 mt-2 text-sm">{error}</p>}
                    </aside>


                    
                    <main className="lg:col-span-2  lg:mt-0">
                        
                        <section className="bg-black/90 p-6 rounded-xl shadow-2xl mb-8 mt-12">
                            <h4 className="text-lg font-medium text-gray-200 mb-2">Résumé (Extrait)</h4>
                            <p className="text-gray-300 min-h-[5rem] border-l-4 border-amber-500 pl-4 py-2">
                                {summary || "Le résumé du texte s'affichera ici après l'analyse."}
                            </p>
                        </section>
                        
                        
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                            
                            
                            <MetricCard 
                                title="Ton Général Détecté" 
                                value={ton.toUpperCase()} 
                                color={ton === 'positif' ? 'green' : ton === 'négatif' ? 'red' : 'blue'}
                                details="Sentiment du texte"
                            />

                            <MetricCard 
                                title="Score de Catégorie" 
                                value={score} 
                                color="blue"
                                details={`Catégorie : ${category}`}
                            />
                            
                            <MetricCard 
                                title="Catégorie Principale" 
                                value={category.toUpperCase()} 
                                color="orange"
                                details={`Score associé : ${score}`}
                            />
                        </div>
                    </main>
                </div>
            </div>
        </div>
    );
}
