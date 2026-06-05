---
layout: default
title: Misoprostol
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 2
---

# Misoprostol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Misoprostol: De Úlcera Gástrica e Indicaciones Obstétricas a Amenorrea

## Resumen en Una Frase

Misoprostol es un análogo sintético de la prostaglandina E1 (PGE1), originalmente utilizado para la prevención de úlceras gástricas inducidas por AINE y para procedimientos obstétrico-ginecológicos (inducción del parto, aborto médico, hemorragia posparto).
El modelo TxGNN predice que podría ser efectivo para **Amenorrea (enfermedad)**,
con **0 ensayos clínicos registrados** y **7 publicaciones** que actualmente respaldan esta dirección de manera indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Prevención de úlcera gástrica por AINE / Indicaciones obstétricas (sin registro en Colombia) |
| Nueva Indicación Predicha | Amenorrea (enfermedad) |
| Puntaje de Predicción TxGNN | 99.64% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✗ No comercializado |
| Número de Registros Sanitarios | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Misoprostol actúa como análogo de la prostaglandina E1 activando los receptores EP1/EP3 del miometrio, lo que induce contracciones uterinas y reblandecimiento cervical. Este mecanismo facilita la expulsión del contenido endometrial retenido.

En el contexto específico de la **amenorrea secundaria por retención de contenido uterino** (aborto diferido, aborto incompleto), existe un apoyo mecanístico directo: al promover la contracción uterina y la expulsión del contenido retenido, misoprostol puede restablecer el flujo menstrual interrumpido. Las publicaciones encontradas documentan su uso en combinación con mifepristona para gestión de embarazos muy tempranos (descritos precisamente como "amenorrea ≤35 días"), lo que comparte la misma vía mecanística.

Sin embargo, para la amenorrea funcional de origen hipotalámico-hipofisario-ovárico, o para la amenorrea primaria, misoprostol no posee actividad reguladora hormonal. En esos subtipos la conexión mecanística es débil. Es probable que TxGNN haya establecido este vínculo a través de nodos de comorbilidad ginecológica compartidos en el grafo de conocimiento, más que por una relación causal directa con la amenorrea como entidad clínica independiente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|------------------------|
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | ECA | Human Reproduction | Mifepristona a dosis bajas + misoprostol administrados antes de la menstruación esperada para prevención de embarazo no deseado; evalúa eficacia en restauración del estado no gestante |
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | ECA | Reproductive Sciences | Mifepristona 75 mg + misoprostol autoadministrado para aborto médico ultra-temprano (amenorrea ≤35 días); n=744 mujeres; evalúa eficacia, seguridad y aceptabilidad |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | ECA | Reproductive Sciences | Dosis decrecientes de mifepristona (150–50 mg) + misoprostol 200 µg para terminación de embarazo ultra-temprano (amenorrea ≤35 días); n=2.500 mujeres; aborto completo sin intervención quirúrgica como endpoint primario |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | ECA | J Obstet Gynaecol Research | Mifepristona a dosis bajas + misoprostol autoadministrado para terminación de embarazo temprano; investiga seguridad y eficacia del esquema de autoadministración domiciliaria |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Revisión | J Obstet Gynaecol Canada | Ablación endometrial para hemorragia uterina anormal; misoprostol como preparación cervical preoperatoria; hasta 30% de mujeres en edad reproductiva buscan atención por esta causa |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Serie de Casos | BMJ | Manejo médico de aborto diferido y embarazo anembriogénico con misoprostol; uno de los primeros reportes de uso ginecológico del fármaco |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Reporte de Caso | Cureus | Hígado graso agudo del embarazo con amenorrea como síntoma de presentación (no como indicación de tratamiento con misoprostol); relevancia indirecta |

---

## Información de Mercado en Colombia

Misoprostol no cuenta con registros sanitarios INVIMA vigentes en Colombia. No se encontraron licencias de comercialización activas para este principio activo en la consulta realizada.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción TxGNN presenta respaldo mecanístico parcial y válido únicamente para el subtipo de amenorrea secundaria por retención uterina, pero la evidencia disponible es indirecta: los ECAs encontrados estudian el aborto médico temprano (donde "amenorrea" describe la duración del embarazo, no la condición a tratar), y no existen ensayos clínicos que evalúen misoprostol específicamente para amenorrea como indicación primaria. La ausencia de registro en Colombia agrega una barrera regulatoria adicional.

**Para avanzar se necesita:**
- Ensayos clínicos prospectivos que evalúen misoprostol específicamente para amenorrea secundaria de causa uterina (retención de productos)
- Obtención del perfil MOA completo desde DrugBank para confirmar la plausibilidad mecanística formal
- Información de seguridad y contraindicaciones del prospecto oficial (datos actualmente no disponibles)
- Definición clara del subtipo de amenorrea objetivo antes de cualquier desarrollo clínico, dado que el mecanismo solo aplica a la etiología uterina y no a la funcional u hormonal
- Evaluación de viabilidad regulatoria para obtener registro sanitario INVIMA si se decide avanzar en Colombia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

