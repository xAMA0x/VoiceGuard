---
title: "VoiceGuard"
description: "Déverrouillage de session Windows par la voix (Python + module Windows natif)."
date: "2024-09-20"
tags: ["python","security","whisper","biometrics","windows"]
lang: "fr"

# Configuration techStack
techStack:
  - name: "Python"
    category: "language"
    icon: "🐍"
  - name: "C++"
    category: "language"
    icon: "💿"
  - name: "Whisper (OpenAI)"
    category: "tool"
    icon: "🎙️"
  - name: "PyAudio"
    category: "tool"
    icon: "🎧"
  - name: "Tkinter"
    category: "framework"
    icon: "🖼️"
  - name: "Asyncio"
    category: "tool"
    icon: "⚡"
  - name: "Windows Credential Provider"
    category: "security"
    icon: "🪟"

# Architecture du projet
architecture:
  overview: "L'architecture est une solution client-serveur locale sophistiquée. Un module C++ (VoiceGuard_Credential_Provider) s'intègre au plus bas niveau de Windows (écran de connexion). Un service Python (App/) tourne en arrière-plan, gérant la capture audio (PyAudio), la transcription (Whisper), et la comparaison de la phrase secrète. Les deux composants communiquent via un canal IPC (sockets TCP locaux) pour envoyer la commande de déverrouillage."
  components:
    - "VoiceGuard_Credential_Provider (C++) : Module d'authentification natif (.dll) qui s'enregistre dans Windows pour s'afficher comme une option de connexion sur l'écran de verrouillage."
    - "Service d'arrière-plan Python (App/main_app.py) : Service Python (Asyncio) qui tourne en continu. Il écoute les connexions du module C++ et contient le modèle Whisper."
    - "Canal de Communication IPC (Sockets) : Un socket TCP (localhost:PORT) qui sert de pont. Le module C++ (client) envoie l'audio au service Python (serveur) et attend une réponse OK/KO."
    - "App/main_tk.py (GUI d'enrôlement) : Application de configuration (Tkinter) que l'utilisateur lance pour enregistrer sa 'phrase secrète' via Whisper."
    - "Module de capture audio (PyAudio) : Bibliothèque Python utilisée à la fois par l'application d'enrôlement et par le service de connexion pour écouter l'utilisateur."

# Diagrammes d'architecture (optionnel)
diagrams:
  - path: "https://raw.githubusercontent.com/xAMA0x/VoiceGuard/main/.portfolio/diagrams/diagram.svg"
    title: "Architecture Hybride (C++ / Python)"
    description: "Flux de communication entre le module C++ (Credential Provider) et le service Python (Whisper) via IPC"

# URLs et liens
demo_url: ""
demo_label: ""
github_url: "https://github.com/xAMA0x/VoiceGuard"
---

## 🎯 Vue d'ensemble

<div class="overview-hero dark:bg-gradient-to-br dark:from-accent/10 dark:to-purple-900/10 bg-gradient-to-br from-indigo-50 to-purple-50 border dark:border-accent/20 border-indigo-200 rounded-2xl p-8 my-8 shadow-lg">
  <p class="text-lg dark:text-white/90 text-slate-700 leading-relaxed mb-6">
    VoiceGuard réinvente la sécurité Windows en intégrant l'authentification biométrique vocale directement sur l'écran de connexion. Ce projet combine un <strong>module C++ natif</strong> (<code>Credential Provider</code>) avec la puissance de <strong>Python</strong> et du modèle <strong>Whisper d'OpenAI</strong> pour la reconnaissance vocale. Le résultat est un système de déverrouillage <strong>sécurisé</strong> et <strong>personnel</strong> où votre voix devient votre mot de passe.
  </p>
  
  <div class="stats-row grid grid-cols-2 md:grid-cols-4 gap-4 mt-6">
    <div class="stat-item text-center">
      <div class="stat-value text-3xl font-bold dark:text-accent text-indigo-600">5</div>
      <div class="stat-label text-sm dark:text-white/60 text-slate-600">Collaborateurs (Projet ESGI)</div>
    </div>
    <div class="stat-item text-center">
      <div class="stat-value text-3xl font-bold dark:text-accent text-indigo-600">1</div>
      <div class="stat-label text-sm dark:text-white/60 text-slate-600">Modèle IA (Whisper)</div>
    </div>
    <div class="stat-item text-center">
      <div class="stat-value text-3xl font-bold dark:text-accent text-indigo-600">1</div>
      <div class="stat-label text-sm dark:text-white/60 text-slate-600">Fournisseur d'identification Windows</div>
    </div>
    <div class="stat-item text-center">
      <div class="stat-value text-3xl font-bold dark:text-accent text-indigo-600">2</div>
      <div class="stat-label text-sm dark:text-white/60 text-slate-600">Composants (C++ / Python)</div>
    </div>
  </div>
</div>

### Objectifs du projet

<div class="objectives-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 my-8">
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🎓
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Défi Académique (ESGI)
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Répondre à l'exigence d'un projet annuel à gros coefficient (9 mois). Le sujet libre (VoiceGuard) a été choisi pour sa complexité.
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🤝
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Gestion de Projet (5 étudiants)
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Coordonner une équipe de 5 personnes sur un projet long, en répartissant les tâches entre les pôles C++ bas-niveau et backend Python.
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🪟
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Intégration Système (C++)
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Couvrir le sujet 'programmation système' en développant un 'Credential Provider' C++ natif s'intégrant à l'écran de connexion Windows.
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🎙️
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Implémentation IA & Python
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Couvrir le sujet 'IA' en mettant en œuvre un modèle de reconnaissance vocale (Whisper) pour l'authentification en Python.
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      ⚡
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Communication Inter-Processus (IPC)
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Concevoir un canal de communication (Sockets `localhost`) pour que le module C++ (contexte OS) puisse dialoguer avec le service Python.
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🔐
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Solution d'Authentification Complète
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Livrer un PoC fini, incluant l'application d'enrôlement (GUI Tkinter) et le module de déverrouillage fonctionnel.
    </p>
  </div>
</div>

## 🪟 Module C++ (Credential Provider)

<div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 my-8">
  <p class="text-sm dark:text-white/70 text-slate-600 leading-relaxed mb-4">
    C'est le cœur du projet. Un module <strong>C++ natif</strong> compilé en <code>.dll</code> qui utilise l'API <strong>Windows Credential Provider</strong> (V2). Il est conçu pour s'enregistrer auprès du système d'exploitation (via des clés de registre) et s'afficher comme une "tuile" d'authentification personnalisée sur l'écran de connexion Windows.
  </p>
  <ul class="list-disc list-outside space-y-2 pl-5 text-sm dark:text-white/70 text-slate-600">
    <li><strong>Intégration Windows (COM) :</strong> Le module implémente les interfaces COM requises par Windows, notamment <code>ICredentialProvider</code> (pour énumérer les tuiles) et <code>ICredentialProviderCredential</code>.</li>
    <li><strong>Enregistrement de la <code>.dll</code> :</strong> Le module C++ est enregistré dans le Registre Windows sous <code>HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential Providers\</code> pour être chargé par <code>LogonUI.exe</code>.</li>
    <li><strong>Capture audio (bas-niveau) :</strong> Depuis l'écran de connexion, le C++ initie la capture audio (probablement via l'API <strong>WASAPI</strong>) lorsque l'utilisateur clique sur la tuile VoiceGuard.</li>
    <li><strong>Client IPC (Socket) :</strong> Il agit comme un client léger. Il envoie le flux audio capturé au service Python (serveur) via un <strong>socket TCP local</strong> (<code>localhost:PORT</code>).</li>
    <li><strong>Gestion de la réponse :</strong> Il attend une réponse "OK" ou "KO" du service Python. Si "OK", il utilise la fonction <code>LogonUser</code> de Windows pour finaliser le déverrouillage.</li>
  </ul>
</div>

## 🐍 Service Python & IA (Whisper)

<div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 my-8">
  <p class="text-sm dark:text-white/70 text-slate-600 leading-relaxed mb-4">
    C'est le "cerveau" de l'opération, fonctionnant comme un service d'arrière-plan. Ce composant est écrit en Python pour tirer parti de l'écosystème IA (Whisper) et de la programmation asynchrone (<code>asyncio</code>) pour gérer les connexions sans bloquer.
  </p>
  <ul class="list-disc list-outside space-y-2 pl-5 text-sm dark:text-white/70 text-slate-600">
    <li><strong>Serveur <code>asyncio</code> :</strong> Le script <code>main_app.py</code> utilise <code>asyncio.start_server</code> pour ouvrir un socket TCP sur <code>localhost</code>. Il écoute en permanence les connexions venant du module C++.</li>
    <li><strong>Chargement du modèle IA :</strong> Au démarrage, le service charge le modèle <strong>Whisper d'OpenAI</strong> (par exemple, le modèle "base" ou "tiny") en mémoire, prêt pour la transcription.</li>
    <li><strong>Transcription & Comparaison :</strong> Il exécute <code>whisper.transcribe()</code> sur le fichier audio reçu. Le texte résultant est ensuite comparé (après normalisation) à la "phrase secrète" de référence de l'utilisateur.</li>
    <li><strong>Réponse (OK/KO) :</strong> Le service renvoie une réponse binaire simple (ex: <code>b"OK"</code> ou <code>b"KO"</code>) au client C++ pour autoriser ou refuser le déverrouillage.</li>
  </ul>
</div>

## ⚡ Communication Inter-Processus (IPC)

<div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 my-8">
  <p class="text-sm dark:text-white/70 text-slate-600 leading-relaxed mb-4">
    Un défi majeur était de faire communiquer le module C++ (context OS sécurisé) avec le script Python (context session utilisateur). La solution est une <strong>communication IPC</strong> via des <strong>sockets TCP locaux</strong>, simulant une architecture client-serveur sur une seule machine.
  </p>
  <ul class="list-disc list-outside space-y-2 pl-5 text-sm dark:text-white/70 text-slate-600">
    <li><strong>Socket TCP (<code>localhost</code>) :</strong> Un socket est ouvert sur <code>127.0.0.1</code> sur un port défini, permettant aux deux processus de communiquer sans être exposés au réseau externe.</li>
    <li><strong>Client (C++) :</strong> Le module Credential Provider agit en tant que client. Il initie la connexion, envoie le flux de données audio brutes au serveur Python, puis se met en attente de la réponse.</li>
    <li><strong>Serveur (Python) :</strong> Le service <code>asyncio</code> agit en tant que serveur. Il accepte la connexion, reçoit le flux de données, le traite, et renvoie la réponse d'authentification.</li>
    <li><strong>Contexte d'exécution :</strong> Le serveur Python doit être lancé (par la GUI d'enrôlement) et tourner en arrière-plan **avant** que l'utilisateur ne verrouille sa session.</li>
  </ul>
</div>

## 🖥️ Application d'Enrôlement (Tkinter)

<div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 my-8">
  <p class="text-sm dark:text-white/70 text-slate-600 leading-relaxed mb-4">
    Pour que le déverrouillage fonctionne, l'utilisateur doit d'abord enregistrer sa "phrase secrète". Cette application compagnon, <code>main_tk.py</code>, fournit l'interface graphique (GUI) nécessaire pour cet enrôlement en utilisant <strong>Tkinter</strong>.
  </p>
  <ul class="list-disc list-outside space-y-2 pl-5 text-sm dark:text-white/70 text-slate-600">
    <li><strong>Interface <code>Tkinter</code> :</strong> Une fenêtre simple avec des boutons ("Enregistrer", "Démarrer le service") et un retour visuel pour guider l'utilisateur.</li>
    <li><strong>Processus d'enrôlement :</strong> L'application utilise <strong><code>PyAudio</code></strong> pour capturer 5 secondes d'audio du microphone.</li>
    <li><strong>Sauvegarde de la référence :</strong> L'audio capturé est envoyé à <strong>Whisper</strong> pour transcription. C'est le **texte transcrit** (ex: "Sésame ouvre toi") qui est sauvegardé comme "phrase secrète" de référence.</li>
    <li><strong>Gestion du service :</strong> La GUI fournit des boutons pour **démarrer** ou **arrêter** le service d'arrière-plan (le serveur <code>asyncio</code>) et le configurer pour se lancer au démarrage de Windows.</li>
  </ul>
</div>

## 🎓 Compétences démontrées

<div class="skills-showcase space-y-6 my-8">
  
  <div class="skill-category dark:bg-gradient-to-r dark:from-indigo-900/30 dark:to-purple-900/30 bg-gradient-to-r from-indigo-50 to-purple-50 border dark:border-indigo-500/30 border-indigo-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">🪟</span>
      <h3 class="text-xl font-bold dark:text-white text-slate-900">Programmation Système (C++/Windows)</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">API Windows Credential Provider</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Implémentation des interfaces COM `ICredentialProvider`.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Manipulation du Registre Windows</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Enregistrement de la .dll (COM) pour `LogonUI.exe`.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Programmation réseau bas-niveau</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Utilisation de Winsock (C++) pour créer le client TCP (IPC).</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Capture audio bas-niveau (WASAPI)</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Capture audio depuis le desktop sécurisé (écran de connexion).</div>
        </div>
      </div>
    </div>
  </div>
  
  <div class="skill-category dark:bg-gradient-to-r dark:from-indigo-900/30 dark:to-purple-900/30 bg-gradient-to-r from-indigo-50 to-purple-50 border dark:border-indigo-500/30 border-indigo-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">🐍</span>
      <h3 class="text-xl font-bold dark:text-white text-slate-900">Architecture Hybride (Python/IPC)</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Serveur TCP asynchrone</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Utilisation de `asyncio.start_server` pour un service non-bloquant.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Conception IPC</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Pont C++ / Python via Sockets `localhost`.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Gestion de service Python</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Service d'arrière-plan gérant les requêtes d'authentification.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Application GUI (Tkinter)</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Interface d'enrôlement (`main_tk.py`).</div>
        </div>
      </div>
    </div>
  </div>

  <div class="skill-category dark:bg-gradient-to-r dark:from-indigo-900/30 dark:to-purple-900/30 bg-gradient-to-r from-indigo-50 to-purple-50 border dark:border-indigo-500/30 border-indigo-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">🎙️</span>
      <h3 class="text-xl font-bold dark:text-white text-slate-900">Intelligence Artificielle (Whisper)</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Implémentation d'un modèle ASR</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Chargement et exécution de `whisper.transcribe()` d'OpenAI.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Traitement audio (PyAudio)</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Capture et formatage (`.wav`) pour le modèle Whisper.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Logique d'authentification vocale</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Comparaison normalisée du texte transcrit vs référence.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Optimisation de modèle IA</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Choix d'un modèle léger (`base`/`tiny`) pour la réactivité.</div>
        </div>
      </div>
    </div>
  </div>
  
  <div class="skill-category dark:bg-gradient-to-r dark:from-indigo-900/30 dark:to-purple-900/30 bg-gradient-to-r from-indigo-50 to-purple-50 border dark:border-indigo-500/30 border-indigo-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">🤝</span>
      <h3 class="text-xl font-bold dark:text-white text-slate-900">Gestion de Projet (Équipe de 5)</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Architecture multi-composants</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Définition des frontières et de l'API (socket) entre les équipes.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Coordination technique (5 étudiants)</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Gestion Git sur un projet hybride C++/Python.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Cadrage et R&D (Projet annuel)</div>
          <div class="text-xs dark:text-white/60 text-slate-600">R&D sur le Windows Credential Provider.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Polyvalence technique ("Full Stack OS")</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Maîtrise de la chaîne C++ (OS) à Python (IA).</div>
        </div>
      </div>
    </div>
  </div>

</div>

## 📚 Ressources & Documentation

<div class="documentation-grid grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
  
  <div class="doc-card dark:bg-gradient-to-br dark:from-slate-900/50 dark:to-slate-800/50 bg-gradient-to-br from-slate-50 to-slate-100 border dark:border-white/10 border-slate-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300 cursor-pointer" data-doc-type="details">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">📖</span>
      <h3 class="text-lg font-bold dark:text-white text-slate-900">Documentation complète</h3>
    </div>
    <ul class="space-y-3">
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Intégration du Credential Provider C++</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Protocole de communication IPC (Socket)</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Fonctionnement du service Python (Whisper)</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Procédure d'installation et d'enrôlement</span>
      </li>
    </ul>
    <div class="mt-4 text-center">
      <span class="text-sm dark:text-blue-400 text-blue-600 font-semibold">→ Voir les détails techniques</span>
    </div>
  </div>

  <div class="doc-card dark:bg-gradient-to-br dark:from-purple-900/30 dark:to-indigo-900/30 bg-gradient-to-br from-purple-50 to-indigo-50 border dark:border-purple-500/30 border-purple-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300 cursor-pointer" data-doc-type="architecture">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">🗺️</span>
      <h3 class="text-lg font-bold dark:text-white text-slate-900">Diagramme interactif</h3>
    </div>
    <p class="dark:text-white/70 text-slate-600 mb-4">Visualisation complète de l'architecture avec tooltips détaillés pour chaque composant.</p>
    <div class="flex flex-wrap gap-2 mb-4">
      <span class="px-3 py-1 dark:bg-blue-500/20 bg-blue-200 dark:text-blue-300 text-blue-700 rounded-full text-xs">C++ (OS)</span>
      <span class="px-3 py-1 dark:bg-red-500/20 bg-red-200 dark:text-red-300 text-red-700 rounded-full text-xs">Python (IA)</span>
      <span class="px-3 py-1 dark:bg-purple-500/20 bg-purple-200 dark:text-purple-300 text-purple-700 rounded-full text-xs">IPC (Socket)</span>
      <span class="px-3 py-1 dark:bg-green-500/20 bg-green-200 dark:text-green-300 text-green-700 rounded-full text-xs">Sécurité</span>
    </div>
    <div class="text-center">
      <span class="text-sm dark:text-purple-400 text-purple-600 font-semibold">→ Voir l'architecture</span>
    </div>
  </div>

</div>

<script is:inline>
  document.addEventListener('DOMContentLoaded', function() {
    const docCards = document.querySelectorAll('[data-doc-type]');
    docCards.forEach(card => {
      card.addEventListener('click', function() {
        const type = this.getAttribute('data-doc-type');
        const tabButton = document.querySelector(`[data-tab="${type}"]`);
        if (tabButton) {
          tabButton.click();
        }
      });
    });
  });
</script>

---

**Archivé** | **Application Bureau (Windows)** | **Projet Académique (ESGI)**
