---
layout: default
title: Terconazole
parent: Evidencia Alta (L1-L2)
nav_order: 617
evidence_level: L1
indication_count: 10
---

# Terconazole
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Terconazol: De Antifúngico Vaginal con Dexametasona a Vulvitis

## Resumen en Una Frase

Terconazol es un antifúngico triazólico de uso vaginal, comercializado en Colombia en combinación con dexametasona (cremas vaginales) para infecciones vaginales.
El modelo TxGNN predice que podría ser efectivo para **vulvitis** (puntaje 99.84%), con **4 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección, aunque en la práctica corresponde sobre todo a su uso antifúngico ya conocido (candidiasis vulvovaginal) y no a un reposicionamiento genuino.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Terconazol - Dexametasona (combinación con antibiótico/corticoide) |
| Nueva Indicación Predicha | Vulvitis |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (todos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

*Nota: la predicción de mayor puntaje del modelo es vaginitis tricomonal (99.86%), pero solo tiene nivel de evidencia L5 y un vínculo mecanístico débil, por lo que este informe se centra en la primera predicción con evidencia sólida: vulvitis.*

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento farmacológico general, terconazol es un antifúngico triazólico que inhibe la enzima fúngica CYP51 (lanosterol 14-alfa-desmetilasa) y, con ello, la síntesis de ergosterol, un componente esencial de la membrana del hongo.

La vulvitis tiene como causa infecciosa principal la candidiasis vulvovaginal, precisamente la infección que terconazol trata. Por ello la predicción es razonable, pero es esencialmente el uso antifúngico ya establecido y no un reposicionamiento propiamente dicho. La evidencia aplica a la vulvitis de origen candidiásico, no a las vulvitis no infecciosas (por ejemplo, dermatitis de contacto o inflamatoria).

Otras predicciones del modelo tienen poco sustento mecanístico y probablemente reflejan cercanía en la red de conocimiento con "vaginitis": vaginitis tricomonal, vaginitis atrófica posmenopáusica, vulvovaginitis herpética, úlcera vulvar y neoplasia vulvar (todas con nivel L5 y sin ensayos). La vaginosis bacteriana tampoco es esperable que responda a un antifúngico.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02180100](https://clinicaltrials.gov/study/NCT02180100) | Fase 4 | Completado | 140 | Supositorio vaginal de terconazol vs fluconazol en candidiasis vulvovaginal grave; busca demostrar seguridad y eficacia comparables |
| [NCT03473418](https://clinicaltrials.gov/study/NCT03473418) | Fase 3 | Desconocido | 69 | Gel in situ de ketoconazol vs crema de terconazol en candidiasis vaginal (terconazol como comparador) |
| [NCT00803738](https://clinicaltrials.gov/study/NCT00803738) | N/A | Completado | 572 | Equivalencia clínica de dos supositorios de terconazol 80 mg en candidiasis vulvovaginal |
| [NCT04208555](https://clinicaltrials.gov/study/NCT04208555) | N/A | Desconocido | 76 | Ácido bórico vs terconazol en candidiasis vulvovaginal recurrente |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25877666](https://pubmed.ncbi.nlm.nih.gov/25877666/) | 2015 | ECA | Medical Mycology | Supositorio de terconazol (6 días) vs fluconazol oral en candidiasis vulvovaginal grave (140 pacientes) |
| [2381618](https://pubmed.ncbi.nlm.nih.gov/2381618/) | 1990 | ECA | Obstetrics and Gynecology | Crema de terconazol 0.8% vs 1.6% frente a placebo en candidiasis vulvovaginal persistente |
| [3520601](https://pubmed.ncbi.nlm.nih.gov/3520601/) | 1986 | ECA | Pharmatherapeutica | Terconazol vs clotrimazol en tabletas vaginales (60 pacientes) |
| [1941796](https://pubmed.ncbi.nlm.nih.gov/1941796/) | 1991 | Ensayo aleatorizado doble ciego | J Reprod Med | Terconazol 0.4% y 0.8% vs miconazol 2%; curación combinada de 87.9%, 83.8% y 81.3% (900 pacientes) |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Revisión | Expert Rev Anti Infect Ther | Opciones de tratamiento azólico no invasivo para candidiasis vulvovaginal |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Revisión | J Womens Health | Evidencia clínica del ácido bórico en candidiasis vulvovaginal recurrente |
| [2680088](https://pubmed.ncbi.nlm.nih.gov/2680088/) | 1989 | Revisión | Clin Ther | Terconazol como nuevo antifúngico; estudios con unas 5,500 mujeres |
| [11220485](https://pubmed.ncbi.nlm.nih.gov/11220485/) | 2000 | Cohorte retrospectiva | Infect Dis Obstet Gynecol | Crema de terconazol en vaginitis por Candida no albicans |
| [2275233](https://pubmed.ncbi.nlm.nih.gov/2275233/) | 1990 | Revisión comparativa | DICP | Eficacia comparada de fármacos y esquemas para candidiasis vulvovaginal |
| [10546257](https://pubmed.ncbi.nlm.nih.gov/10546257/) | 1999 | Revisión | Nurse Practitioner | Manejo general de la vaginitis (bacteriana, fúngica y protozoaria) |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20265420 | DECADRON T® (cancelado) | Crema vaginal | Terconazol - Dexametasona |
| 20135424 | TEREX-3 (cancelado) | Crema vaginal | Dexametasona y antibióticos |
| 20013336 | VAGICORT® Crema Vaginal (cancelado) | Crema vaginal | Terconazol - Dexametasona |

---

## Citotoxicidad

No aplica: terconazol no es un fármaco antineoplásico, por lo que esta sección se omite.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los datos compilados no encontraron interacciones farmacológicas registradas. Entre la literatura hay un reporte de caso de reacción sistémica (escalofríos, fatiga, opresión torácica y aumento de leucocitos y marcadores inflamatorios) tras un supositorio vaginal de terconazol, lo que sugiere vigilar la tolerancia.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ECA y ensayos de Fase 3 y 4 que respaldan la eficacia de terconazol en la candidiasis vulvovaginal, principal causa infecciosa de vulvitis. Sin embargo, esto equivale al uso antifúngico ya aprobado y no a una indicación nueva; además, los tres registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Confirmar el patógeno (Candida) antes de usarlo; no es útil en vulvitis no infecciosa, bacteriana, protozoaria ni viral.
- Considerar la menor susceptibilidad de especies de Candida no albicans.
- Obtener el prospecto con advertencias y contraindicaciones (actualmente faltan).
- Completar los datos del mecanismo de acción.
- Aclarar la viabilidad regulatoria en Colombia, dado que no hay registros vigentes.
- Mantener en espera (Hold) las demás predicciones sin evidencia (vaginitis tricomonal, vaginitis atrófica, herpética, úlcera y neoplasia vulvar, vaginosis bacteriana).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

