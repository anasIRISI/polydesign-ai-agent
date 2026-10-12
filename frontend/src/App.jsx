
import { useEffect, useRef, useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import "./App.css";

const API_URL = "http://127.0.0.1:8000/chat";

function createConversation() {
  return {
    id: crypto.randomUUID(),
    sessionId: crypto.randomUUID(),
    title: "Nouvelle conversation",
    messages: [],
  };
}

function App() {
  const initialConversation = useRef(createConversation()).current;

  const [conversations, setConversations] = useState([
    initialConversation,
  ]);

  const [activeConversationId, setActiveConversationId] = useState(
    initialConversation.id
  );

  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);

  const [editingMessageIndex, setEditingMessageIndex] = useState(null);
  const [editingText, setEditingText] = useState("");

  const [copiedMessageIndex, setCopiedMessageIndex] = useState(null);

  const messagesEndRef = useRef(null);
  const textareaRef = useRef(null);

  const activeConversation = conversations.find(
    (conversation) => conversation.id === activeConversationId
  );

  /* =========================================================
     AUTO SCROLL
  ========================================================= */

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [activeConversation?.messages, loading]);

  /* =========================================================
     AUTO FOCUS
  ========================================================= */

  useEffect(() => {
    if (!loading) {
      textareaRef.current?.focus();
    }
  }, [activeConversationId, loading]);

  /* =========================================================
     NOUVELLE CONVERSATION
  ========================================================= */

  const newConversation = () => {
    if (loading) return;

    const conversation = createConversation();

    setConversations((previous) => [
      conversation,
      ...previous,
    ]);

    setActiveConversationId(conversation.id);

    setQuestion("");
    setEditingMessageIndex(null);
    setEditingText("");
  };

  /* =========================================================
     CHANGER DE CONVERSATION
  ========================================================= */

  const selectConversation = (id) => {
    if (loading) return;

    setActiveConversationId(id);

    setQuestion("");
    setEditingMessageIndex(null);
    setEditingText("");
  };

  /* =========================================================
     COPIER
  ========================================================= */

  const copyMessage = async (content, index) => {
    try {
      await navigator.clipboard.writeText(content);

      setCopiedMessageIndex(index);

      window.setTimeout(() => {
        setCopiedMessageIndex(null);
      }, 1800);
    } catch (error) {
      console.error(
        "Impossible de copier le message :",
        error
      );
    }
  };

  /* =========================================================
     MODIFIER
  ========================================================= */

  const startEditingMessage = (message, index) => {
    if (loading) return;

    setEditingMessageIndex(index);
    setEditingText(message.content);
  };

  const cancelEditing = () => {
    setEditingMessageIndex(null);
    setEditingText("");
  };

  /* =========================================================
     AJOUT REPONSE ASSISTANT
  ========================================================= */

  const addAssistantMessage = (
    conversationId,
    content
  ) => {
    setConversations((previous) =>
      previous.map((conversation) =>
        conversation.id === conversationId
          ? {
              ...conversation,
              messages: [
                ...conversation.messages,
                {
                  role: "assistant",
                  content,
                },
              ],
            }
          : conversation
      )
    );
  };

  /* =========================================================
     ENVOYER
  ========================================================= */

  const sendMessage = async (
    customQuestion = null
  ) => {
    const text = (
      customQuestion !== null
        ? customQuestion
        : question
    ).trim();

    if (
      !text ||
      loading ||
      !activeConversation
    ) {
      return;
    }

    const conversationId =
      activeConversation.id;

    const sessionId =
      activeConversation.sessionId;

    /* Ajouter question */

    setConversations((previous) =>
      previous.map((conversation) => {
        if (
          conversation.id !==
          conversationId
        ) {
          return conversation;
        }

        const isFirstMessage =
          conversation.messages.length === 0;

        let title =
          conversation.title;

        if (isFirstMessage) {
          title =
            text.length > 42
              ? `${text.substring(
                  0,
                  42
                )}…`
              : text;
        }

        return {
          ...conversation,
          title,
          messages: [
            ...conversation.messages,
            {
              role: "user",
              content: text,
            },
          ],
        };
      })
    );

    setQuestion("");
    setEditingMessageIndex(null);
    setEditingText("");
    setLoading(true);

    try {
      const response = await fetch(
        API_URL,
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json",
          },

          body: JSON.stringify({
            question: text,
            session_id: sessionId,
          }),
        }
      );

      if (!response.ok) {
        throw new Error(
          `Erreur HTTP : ${response.status}`
        );
      }

      const data =
        await response.json();

      addAssistantMessage(
        conversationId,
        data.response
      );
    } catch (error) {
      console.error(error);

      addAssistantMessage(
        conversationId,
        "Je n’arrive pas à contacter le serveur. Vérifiez que FastAPI est bien lancé, puis réessayez."
      );
    } finally {
      setLoading(false);
    }
  };

  /* =========================================================
     MODIFIER + ENVOYER
  ========================================================= */

  const submitEditedMessage = async () => {
    const text =
      editingText.trim();

    if (
      !text ||
      loading ||
      !activeConversation ||
      editingMessageIndex === null
    ) {
      return;
    }

    const conversationId =
      activeConversation.id;

    const sessionId =
      activeConversation.sessionId;

    const editedIndex =
      editingMessageIndex;

    setConversations((previous) =>
      previous.map((conversation) => {
        if (
          conversation.id !==
          conversationId
        ) {
          return conversation;
        }

        return {
          ...conversation,
          messages: [
            ...conversation.messages.slice(
              0,
              editedIndex
            ),
            {
              role: "user",
              content: text,
            },
          ],
        };
      })
    );

    setEditingMessageIndex(null);
    setEditingText("");
    setQuestion("");
    setLoading(true);

    try {
      const response = await fetch(
        API_URL,
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json",
          },

          body: JSON.stringify({
            question: text,
            session_id: sessionId,
          }),
        }
      );

      if (!response.ok) {
        throw new Error(
          `Erreur HTTP : ${response.status}`
        );
      }

      const data =
        await response.json();

      addAssistantMessage(
        conversationId,
        data.response
      );
    } catch (error) {
      console.error(error);

      addAssistantMessage(
        conversationId,
        "Je n’arrive pas à contacter le serveur. Vérifiez que FastAPI est bien lancé, puis réessayez."
      );
    } finally {
      setLoading(false);
    }
  };

  /* =========================================================
     RETRY
  ========================================================= */

  const retryMessage = (index) => {
    if (
      loading ||
      !activeConversation
    ) {
      return;
    }

    for (
      let i = index - 1;
      i >= 0;
      i--
    ) {
      if (
        activeConversation
          .messages[i]
          .role === "user"
      ) {
        sendMessage(
          activeConversation
            .messages[i]
            .content
        );

        return;
      }
    }
  };

  /* =========================================================
     TEXTAREA
  ========================================================= */

  const handleTextareaInput = (
    event
  ) => {
    setQuestion(
      event.target.value
    );

    event.target.style.height =
      "auto";

    event.target.style.height =
      `${Math.min(
        event.target.scrollHeight,
        180
      )}px`;
  };

  /* =========================================================
     ENTER
  ========================================================= */

  const handleKeyDown = (
    event
  ) => {
    if (
      event.key === "Enter" &&
      !event.shiftKey
    ) {
      event.preventDefault();

      sendMessage();
    }
  };

  /* =========================================================
     SUGGESTIONS
  ========================================================= */

  const handleSuggestion = (
    text
  ) => {
    if (loading) return;

    setQuestion(text);

    textareaRef.current?.focus();
  };

  /* =========================================================
     RENDER
  ========================================================= */

  return (
    <div className="app">

      {/* =====================================================
          SIDEBAR
      ===================================================== */}

      <aside className="sidebar">

        <div className="brand">

          <div
            className="brand-mark"
            aria-hidden="true"
          >
            <span />
            <span />
            <span />
          </div>

          <div>
            <div className="brand-name">
              Polydesign AI
            </div>

            <div className="brand-subtitle">
              Assistant industriel
            </div>
          </div>

        </div>

        <button
          className="new-conversation"
          onClick={newConversation}
          disabled={loading}
        >
          <span className="new-icon">
            +
          </span>

          <span>
            Nouvelle conversation
          </span>
        </button>

        <div className="conversation-list">

          <div className="sidebar-section-title">
            Conversations
          </div>

          {conversations.map(
            (conversation) => (
              <button
                key={conversation.id}
                className={`conversation-item ${
                  conversation.id ===
                  activeConversationId
                    ? "active"
                    : ""
                }`}
                onClick={() =>
                  selectConversation(
                    conversation.id
                  )
                }
                disabled={loading}
              >

                <span className="conversation-icon">
                  ◌
                </span>

                <span className="conversation-label">
                  {conversation.title}
                </span>

              </button>
            )
          )}

        </div>

        <div className="sidebar-footer">

          <span className="status-dot" />

          <span>
            Système opérationnel
          </span>

        </div>

      </aside>

      {/* =====================================================
          CHAT
      ===================================================== */}

      <main className="chat-section">

        <header className="chat-header">

          <div className="header-context">

            <div className="header-icon">
              AI
            </div>

            <div>

              <div className="header-title">
                {activeConversation?.title ||
                  "Polydesign AI"}
              </div>

              <div className="header-status">

                <span className="online-dot" />

                Agent connecté

              </div>

            </div>

          </div>

          <div className="header-badge">
            IA industrielle
          </div>

        </header>

        {/* ===================================================
            MESSAGES
        =================================================== */}

        <div className="messages">

          {/* =================================================
              WELCOME
          ================================================= */}

          {activeConversation?.messages
            .length === 0 && (

            <div className="welcome">

              <div
                className="welcome-mark"
                aria-hidden="true"
              >
                <span />
                <span />
                <span />
              </div>

              <h1>
                Bonjour, comment puis-je
                vous aider ?
              </h1>

              <p>
                Interrogez vos données
                industrielles et vos
                documents d’entreprise
                en langage naturel.
              </p>

              <div className="suggestions">

                <button
                  onClick={() =>
                    handleSuggestion(
                      "Quelle est l'efficience de la cellule 19 ?"
                    )
                  }
                >
                  <strong>
                    Efficience
                  </strong>

                  <span>
                    Analyser une cellule
                  </span>
                </button>

                <button
                  onClick={() =>
                    handleSuggestion(
                      "Quelle est la dernière présence du matricule 6311 ?"
                    )
                  }
                >
                  <strong>
                    Présence
                  </strong>

                  <span>
                    Consulter un employé
                  </span>
                </button>

                <button
                  onClick={() =>
                    handleSuggestion(
                      "Comment faire un reset de SYSPRO PASSWORD ?"
                    )
                  }
                >
                  <strong>
                    Documents
                  </strong>

                  <span>
                    Rechercher une procédure
                  </span>
                </button>

              </div>

            </div>
          )}

          {/* =================================================
              MESSAGE LIST
          ================================================= */}

          {activeConversation?.messages.map(
            (message, index) => {

              const isEditing =
                editingMessageIndex ===
                index;

              return (

                <article
                  key={`${activeConversation.id}-${index}`}
                  className={`message ${
                    message.role ===
                    "user"
                      ? "user-message"
                      : "assistant-message"
                  }`}
                >

                  <div className="message-avatar">
                    {message.role ===
                    "user"
                      ? "U"
                      : "AI"}
                  </div>

                  <div className="message-body">

                    <div className="message-topline">

                      <span className="message-role">

                        {message.role ===
                        "user"
                          ? "Vous"
                          : "Polydesign AI"}

                      </span>

                    </div>

                    <div className="message-content">

                      {isEditing ? (

                        <textarea
                          className="edit-message-input"
                          value={
                            editingText
                          }
                          onChange={(
                            event
                          ) =>
                            setEditingText(
                              event.target
                                .value
                            )
                          }
                          onKeyDown={(
                            event
                          ) => {

                            if (
                              event.key ===
                                "Enter" &&
                              !event.shiftKey
                            ) {

                              event.preventDefault();

                              submitEditedMessage();

                            }

                          }}
                          autoFocus
                        />

                      ) : message.role ===
                        "assistant" ? (

                        <ReactMarkdown
                          remarkPlugins={[
                            remarkGfm,
                          ]}
                        >
                          {
                            message.content
                          }
                        </ReactMarkdown>

                      ) : (

                        <div className="user-text">
                          {
                            message.content
                          }
                        </div>

                      )}

                    </div>

                    {/* ACTIONS */}

                    <div className="message-actions">

                      {isEditing ? (

                        <>

                          <button
                            onClick={
                              cancelEditing
                            }
                            disabled={
                              loading
                            }
                          >
                            Annuler
                          </button>

                          <button
                            className="action-primary"
                            onClick={
                              submitEditedMessage
                            }
                            disabled={
                              loading ||
                              !editingText.trim()
                            }
                          >
                            Enregistrer
                          </button>

                        </>

                      ) : (

                        <>

                          <button
                            onClick={() =>
                              copyMessage(
                                message.content,
                                index
                              )
                            }
                          >
                            {copiedMessageIndex ===
                            index
                              ? "✓ Copié"
                              : "Copier"}
                          </button>

                          {message.role ===
                            "user" && (

                            <button
                              onClick={() =>
                                startEditingMessage(
                                  message,
                                  index
                                )
                              }
                              disabled={
                                loading
                              }
                            >
                              Modifier
                            </button>

                          )}

                          {message.role ===
                            "assistant" && (

                            <button
                              onClick={() =>
                                retryMessage(
                                  index
                                )
                              }
                              disabled={
                                loading
                              }
                            >
                              Réessayer
                            </button>

                          )}

                        </>

                      )}

                    </div>

                  </div>

                </article>

              );
            }
          )}

          {/* =================================================
              LOADING
          ================================================= */}

          {loading && (

            <article className="message assistant-message">

              <div className="message-avatar">
                AI
              </div>

              <div className="message-body">

                <div className="message-topline">

                  <span className="message-role">
                    Polydesign AI
                  </span>

                </div>

                <div
                  className="typing-indicator"
                  aria-label="Réponse en cours"
                >

                  <span />
                  <span />
                  <span />

                  <em>
                    Analyse en cours…
                  </em>

                </div>

              </div>

            </article>

          )}

          <div ref={messagesEndRef} />

        </div>

        {/* ===================================================
            COMPOSER
        =================================================== */}

        <div className="composer-area">

          <div className="input-container">

            <textarea
              ref={textareaRef}
              placeholder="Posez votre question à Polydesign AI…"
              value={question}
              onChange={
                handleTextareaInput
              }
              onKeyDown={
                handleKeyDown
              }
              disabled={loading}
              rows={1}
            />

            <button
              className="send-button"
              onClick={() =>
                sendMessage()
              }
              disabled={
                loading ||
                !question.trim()
              }
              aria-label="Envoyer"
            >

              <span>
                Envoyer
              </span>

              <span className="send-arrow">
                ↑
              </span>

            </button>

          </div>

          <div className="input-hint">
            Entrée pour envoyer ·
            Maj + Entrée pour une
            nouvelle ligne
          </div>

        </div>

      </main>

    </div>
  );
}

export default App;

