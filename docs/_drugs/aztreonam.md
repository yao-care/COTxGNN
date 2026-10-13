---
layout: default
title: Aztreonam
parent: Solo Predicción del Modelo (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
---

# Aztreonam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Aztreonam: De Antibacteriano Monobactámico a Uretritis Gonocócica

## Resumen en Una Frase

Aztreonam es un antibiótico monobactámico, registrado en Colombia bajo el nombre del principio activo, que se usa contra infecciones por bacterias gramnegativas aerobias.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia** (predicción de mayor puntaje), pero esa predicción carece de sustento biológico; la indicación con respaldo más plausible es la **uretritis gonocócica**, con **0 ensayos clínicos registrados** y **6 publicaciones**, en su mayoría estudios antiguos no comparativos.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Aztreonam (el registro sanitario solo indica el nombre del principio activo, sin texto de indicación detallado) |
| Nueva Indicación Predicha (mayor puntaje TxGNN) | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L5 (hiperamilasemia) |
| Indicación con mayor respaldo | Uretritis gonocócica (L3, puntaje TxGNN 99.59%) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

> **Nota:** La predicción de mayor puntaje (hiperamilasemia) es un hallazgo de laboratorio, no una enfermedad infecciosa, y no tiene respaldo mecanístico ni evidencia. Por ello, en este informe se presenta además la indicación mejor respaldada (uretritis gonocócica) como línea de investigación.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según el conocimiento general, aztreonam es un antibiótico monobactámico que inhibe la síntesis de la pared celular bacteriana mediante la unión a la PBP3 en bacterias gramnegativas aerobias.

**Hiperamilasemia (predicción principal):** no existe un vínculo mecanístico plausible. Es un hallazgo de laboratorio y no una infección; el alto puntaje de TxGNN probablemente sea un artefacto del grafo de conocimiento. Sin ensayos ni literatura. Lo mismo aplica a otras predicciones de alto puntaje como síndrome de hiperviscosidad policlonal, analbuminemia congénita, enfermedad hematológica premaligna y gammapatía monoclonal, donde aztreonam no actúa sobre la fisiopatología.

**Uretritis gonocócica (mejor respaldada):** es biológicamente plausible, pues aztreonam actúa sobre *Neisseria gonorrhoeae*, incluidas cepas resistentes a penicilina. Sin embargo, se trata de una extensión de uso antibacteriano más que de un reposicionamiento a un mecanismo nuevo. Sus limitaciones son: ausencia de ensayos aleatorizados, estudios mayormente de los años 80, reportes de gonococos con alta resistencia a aztreonam, y que las guías actuales se basan en otros fármacos. Podría considerarse solo como opción de nicho (alergia a betalactámicos o casos resistentes), pendiente de confirmación en ensayos comparativos modernos.

Otras predicciones con plausibilidad limitada: epiglotitis (probable *Haemophilus influenzae*, sensible a aztreonam, pero con cefalosporinas de tercera generación como estándar) y pielonefritis xantogranulomatosa (infección por gramnegativos, pero con manejo principalmente quirúrgico). Uretritis por *Ureaplasma* es implausible, pues este microorganismo carece de pared celular.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Indicación: uretritis gonocócica.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Ensayo clínico de un solo brazo, abierto | Antimicrob Agents Chemother | Aztreonam 2 g intramuscular en dosis única para *N. gonorrhoeae*, con inclusión de infección faríngea, ante la amenaza de resistencia a ceftriaxona |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Estudio de eficacia clínica | Antimicrob Agents Chemother | Aztreonam 1 g IM vs. espectinomicina 2 g IM en gonorrea no complicada; sin fallos en ninguno de los dos grupos |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Estudio clínico de dosis única | Genitourin Med | Erradicación en 61 hombres y 26 mujeres con 1 g IM, salvo un caso faríngeo; bien tolerado |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Estudio epidemiológico y terapéutico | Hinyokika Kiyo | Estudio japonés de terapia de dosis única con aztreonam en infecciones gonocócicas |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Estudio de efectividad in vitro/clínica | J Infect Dis | Eficacia frente a gonococos productores de penicilinasa |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Vigilancia de resistencia/microbiología | J Infect Chemother | Aparición de *N. gonorrhoeae* con alta resistencia a cefemos y aztreonam, sin producción de betalactamasa |

Otras indicaciones con literatura indirecta:

| PMID | Año | Tipo | Revista | Indicación | Hallazgos Principales |
|------|-----|------|------|---------|---------|
| [3766490](https://pubmed.ncbi.nlm.nih.gov/3766490/) | 1986 | Serie de casos pediátrica | Am J Dis Child | Epiglotitis | 59 niños con infecciones graves por gramnegativos; evidencia indirecta y no específica de epiglotitis |
| [4079014](https://pubmed.ncbi.nlm.nih.gov/4079014/) | 1985 | Estudio clínico | Jpn J Antibiot | Gammapatía monoclonal | Eficacia de 51.1% en infecciones graves asociadas a trastornos hematológicos; uso de soporte antiinfeccioso, no modificación de la enfermedad |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20271484 (cancelado) | AZTREONAM 1G polvo estéril para reconstituir a solución inyectable (Vicar Farmacéutica S.A.) | Polvo estéril para reconstituir a solución inyectable | Aztreonam |
| 20163741 (cancelado) | AZBIOS® 1G (Bioselect S.A.C.I.) | Polvo estéril para reconstituir a solución inyectable | Aztreonam |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto):** enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal y enfermedad bronquial.
- **Interacciones farmacológicas:** se identificaron 27 interacciones en total. Las de nivel moderado incluyen:
  - Ácido picosulfúrico
  - Dicumarol
  - Warfarina

  Otras interacciones, de nivel no clasificado, incluyen vancomicina, amikacina, anfotericina B, fluconazol, tacrolimus, heparina, morfina, inhibidores de bomba de protones (pantoprazol, omeprazol, lansoprazol), hidrocortisona, dexametasona, ondansetrón, metronidazol, ácido acetilsalicílico, salbutamol y aciclovir.

Para advertencias y contraindicaciones del prospecto, consultar el prospecto del producto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de mayor puntaje (hiperamilasemia) no tiene respaldo mecanístico ni evidencia clínica (L5). La indicación mejor respaldada, uretritis gonocócica (L3), se apoya en estudios antiguos no comparativos, con reportes de resistencia, y los registros sanitarios en Colombia están cancelados, por lo que no se justifica avanzar por ahora. Puede mantenerse como pregunta de investigación para casos de alergia a betalactámicos o resistencia.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto (advertencias y contraindicaciones), ya que su ausencia impide el tamizaje de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Ensayos comparativos modernos de aztreonam en gonorrea, con datos de resistencia actuales.
- Evaluar la viabilidad regulatoria y comercial, dado que no hay registros vigentes en Colombia.
- Confirmar la compatibilidad de vías de administración, hoy pendiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

